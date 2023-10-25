import asyncio
import aiohttp
import io
from hashlib import md5
import logging
import numpy as np
from datetime import datetime, timedelta

from PIL import Image
from typing import List, Optional, Dict, Union, Tuple, Any

from ha_core.utils.measurer import track
from ha_core.utils.misc import chunks
from ha_core.config.base import CDN_IP, CDN_SALT, CDN_URL, IS_PRODUCTION
from ha_core.utils import safe_time


N_RETRIES = 1
COOLDOWN = 0
BATCH_SIZE = 500
SUCCESS_RESPONSE_CODE = 200


class DaemonBaseAsync:
    def __init__(self):
        self.session = aiohttp.ClientSession()

    def __del__(self):
        asyncio.get_event_loop().run_until_complete(self.session.close())


class DaemonRestDataAsync(DaemonBaseAsync):
    @track('daemon_rest_async')
    async def get_by_url(
        self, url: str, tag: str, source=None, retries: int = 1, cooldown: Optional[int] = None
    ) -> Tuple[str, int, Any]:
        for _ in range(retries):
            resp = await self.session.request(
                method='GET',
                url=url,
                headers={'User-Agent': 'ds:' + (source or 'rest_service')},
                verify_ssl=False,
            )
            result, status = await resp.read(), resp.status
            if status == 425 and cooldown:
                await asyncio.sleep(cooldown)

        return tag, status, result


def _get_sign(url_path, params, timestamp):
    for key in sorted(params):
        url_path += key + params[key]
    return md5((timestamp + url_path + CDN_SALT).encode()).hexdigest()


def get_cdn_link(
        file_path=None,
        social_name=None,
        social_item=None,
        social_item_id=None,
        width=None,
        height=None,
        till=None,
        use_ip=False,
        longpoll=False,
        dernd=False
):
    """Returns link for HA CDN: file from storage or user avatar or post image

    :param str|None file_path: path for the file from HA storage
    :param str|None social_name: instagram, tiktok, etc
    :param str|None social_item: user or post
    :param str|None social_item_id: user/account social id or post's code
    :param int|None width: width of the image if resize is needed, use only width or height for keeping aspect ratio
    :param int|None height: height of the image if resize is needed, use only width or height for keeping aspect ratio
    :param datetime|None till: valid until datetime
    :param bool use_ip: generate link with ip instead of domain for internal usage

    :return: cdn link
    :rtype: str
    """

    # костыль чтобы ссылки не тухли за час
    till = datetime.utcnow() + timedelta(hours=1)
    timestamp = safe_time.to_timestamp(till or datetime.utcnow())
    timestamp = str(timestamp - timestamp % 3600)

    params = {}
    if width:
        params['w'] = str(width)
    if height:
        params['h'] = str(height)
    if till:
        params['till'] = timestamp

    if file_path:
        url_path = '/ha/' + file_path
    else:
        url_path = f'/img/{social_name}/{social_item}/{social_item_id}.jpg'

    params['sign'] = _get_sign(url_path, params, timestamp)

    if longpoll:
        params['longpoll'] = '1'
    if dernd:
        params['dernd'] = '1'

    host = CDN_URL if not use_ip or not IS_PRODUCTION else CDN_IP

    return host + url_path + '?' + '&'.join(['='.join(i) for i in params.items()])


def get_ig_avatar(social_id: str, big=False, use_ip=False, longpoll=False, dernd=False) -> str:
    if not social_id:
        return ''

    return get_cdn_link(
        social_name='instagram',
        social_item='user',
        social_item_id=social_id,
        width=320 if big else 150,
        use_ip=use_ip,
        longpoll=longpoll,
        dernd=dernd
    )


def m_get_image_contents_with_code(
    urls: Dict[Union[str, int], str],
    source: Optional[str],
    batch_size: int,
    retries: int,
    cooldown: int,
) -> dict:
    daemon_rest_async = DaemonRestDataAsync()
    tasks = [
        daemon_rest_async.get_by_url(url, u_id, source or 'cdn_service', retries, cooldown)
        for u_id, url in urls.items()
    ]
    res = {}
    for chunk in chunks(tasks, batch_size):
        for complete_task in asyncio.get_event_loop().run_until_complete(
            asyncio.gather(*chunk, return_exceptions=True)
        ):
            res[complete_task[0]] = {'status': complete_task[1], 'bin': complete_task[2]}
    return res


@track('get_avatars')
def get_avatars(user_ids: List[str]):
    images = [None for _ in user_ids]
    codes = [-1 for _ in user_ids]

    img_urls = {
        # user_id: get_ig_avatar(user_id, big=True, dernd=True if not precise_detection else False)
        user_id: get_ig_avatar(user_id, big=True, dernd=True)
        for user_id in user_ids
    }
    imgs = m_get_image_contents_with_code(img_urls, 'new_agre_detector', BATCH_SIZE, N_RETRIES, COOLDOWN)

    for i, (user_id, data) in enumerate(imgs.items()):
        if data['status'] == 200:
            if data['bin']:
                img_ = Image.open(io.BytesIO(data['bin']))
                img = np.asarray(img_)
                images[i] = img

            else:
                logging.debug(f"Can't load avatar for account: {user_id}")
                images[i] = None

        elif data['status'] == 425:
            logging.debug("425 code from CDN")

        elif data['status'] == 410:
            logging.debug("410 code from CDN")

        elif data['status'] == 417:
            logging.debug("417 code from CDN")

        codes[i] = data['status']

    return list(img_urls.values()), images, codes


@track('get_ig_post')
def get_ig_post(post_id: str, use_ip=False, longpoll=False, dernd=False) -> str:
    if not post_id:
        return ''

    return get_cdn_link(
        social_name='instagram',
        social_item='post',
        social_item_id=post_id,
        width=480,
        use_ip=use_ip,
        longpoll=longpoll,
        dernd=dernd,
    )


@track('get_post_images')
def get_post_images(posts: List[str]):
    images = {}
    codes = {}
    img_urls = {post: get_ig_post(post, dernd=True) for post in posts}
    imgs = m_get_image_contents_with_code(img_urls, 'new_agre_detector', BATCH_SIZE, N_RETRIES, COOLDOWN)

    for post_id, data in imgs.items():
        if data['status'] == 200:
            if data['bin']:
                img_ = Image.open(io.BytesIO(data['bin']))
                # img = np.asarray(img_)
                images[post_id] = img_
                codes[post_id] = data['status']
            else:
                images[post_id] = None
                codes[post_id] = data['status']

        elif data['status'] == 425:
            images[post_id] = None
            codes[post_id] = data['status']

        elif data['status'] == 410:
            images[post_id] = None
            codes[post_id] = data['status']
        else:
            images[post_id] = None
            codes[post_id] = data['status']

    return img_urls, images, codes
