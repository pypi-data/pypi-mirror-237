import os
from typing import Dict

from ha_core.utils.db import get_hz_db

from constants import LIST_OF_BRANDS, LIST_OF_BRANDS_REVERSED, LIST_OF_BRAND_ACCOUNTS
from dataset.avatars import get_post_images


# def get_user_ids_for_brand(brand_name):
#     user_ids = []
#     cursor = get_db()['instagram_report_data'].find({}, {'_id': True, 'basic.description': True}).limit(1000000)
#     for item in cursor:
#         if brand_name in item['basic']['description'] or brand_name.title() in item['basic']['description']:
#             user_ids.append(item['_id'])
#
#     return user_ids


def get_post_ids_for_brand(brand_name):
    post_ids = []
    cursor = get_hz_db('instagram')['instagram_post'].find({}, {'_id': True, 'caption': True}).limit(1000000)  # todo check collection
    for item in cursor:
        if brand_name in item.get('caption', '').split() or \
                brand_name.title() in item.get('caption', '').split() or \
                '#' + brand_name in item.get('caption', '').split() or \
                '#' + brand_name.lower() in item.get('caption', '').split():
            post_ids.append(item['_id'])

    return post_ids


def get_premium_post_ids_for_brand(brand_name):
    post_ids = []
    brand_account_ids = LIST_OF_BRAND_ACCOUNTS[LIST_OF_BRANDS_REVERSED[brand_name]]
    cursor = get_hz_db('instagram')['instagram_post'].find({'user_id': {'$in': [str(_id) for _id in brand_account_ids]}}, {'_id': True, 'caption': True}).limit(100000)  # todo check collection
    for item in cursor:
        post_ids.append(item['_id'])

    return post_ids


def save_images_to_directory(directory_name,
                             images_by_post_ids):
    valid_post_ids = []

    # Parent Directory path
    parent_dir = '//dataset'

    # Path
    path = os.path.join(parent_dir, 'images')
    if not os.path.exists(path):
        os.mkdir(path)
    path = os.path.join(path, directory_name)
    os.mkdir(path)
    print(path)
    path = os.path.join(parent_dir, 'labels')
    if not os.path.exists(path):
        os.mkdir(path)
    path = os.path.join(path, directory_name)
    os.mkdir(path)
    # os.mkdir('labels/' + directory_name + '/')

    for post_id, image in images_by_post_ids.items():
        if image:
            valid_post_ids.append(post_id)
            save_image(directory_name, post_id, image)

    if valid_post_ids:
        with open('labels/' + directory_name + '/' + 'labels.txt', 'w') as f:
            for post_id in valid_post_ids:
                # write each item on a new line
                f.write("%s\n" % post_id + '.jpg')


def save_image(directory_name, post_id, image):
    image.save('images/' + directory_name + '/' + str(post_id) + '.jpg')


def get_post_ids_for_brands(brand_names: Dict[int, str]):
    for _id, brand_name in brand_names.items():
        print(brand_name)
        post_ids1 = get_post_ids_for_brand(brand_name=brand_name)
        post_ids2 = get_premium_post_ids_for_brand(brand_name=brand_name)
        post_ids = post_ids1 + post_ids2
        print(len(post_ids), post_ids[0])
        img_urls, images_by_post_ids, codes = get_post_images(posts=list(set((post_ids))))
        save_images_to_directory(directory_name=brand_name,
                                 images_by_post_ids=images_by_post_ids)


get_post_ids_for_brands(LIST_OF_BRANDS)
