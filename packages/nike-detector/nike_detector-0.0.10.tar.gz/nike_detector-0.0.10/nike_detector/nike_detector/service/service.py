from typing import Optional

# import pkg_resources
from ultralytics import YOLO
from PIL import Image as Img
import gdown

import torch


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
models = {}
brand_name = 'NIKE'
confidence = 0.5  # todo make config
output_images_dir = 'output'


def init_nike_model():
    # Load a model

    url = 'https://drive.google.com/file/d/1xk3ei6v8qzpeFN9SZXUzQO6ra0tMsdvR/view?usp=drive_link'
    output = 'best_old.pt'
    gdown.download(url, output, quiet=False)

    # url = 'https://drive.google.com/file/d/1xk3ei6v8qzpeFN9SZXUzQO6ra0tMsdvR/view?usp=drive_link'
    # output = 'yolo8x.pt'
    # gdown.download(url, output, quiet=False)

    # data_path = pkg_resources.resource_filename('nike_detector', 'models/')
    models['yolo_model'] = YOLO('yolov8x.yaml')  # build a new model from scratch
    models['yolo_model'] = YOLO('yolov8x.pt')  # load a pretrained model (recommended for training)
    # models['yolo_model'] = YOLO(data_path + 'best_old.pt')
    models['yolo_model'] = YOLO('best_old.pt')
    # logger.info("Trained YOLO model is successfully loaded on: {device}".format(device=device))

    return models['yolo_model']


def predict(image,
            save=True,
            save_txt=True):  # path to img or url
    run_name = 'predict'
    results = models['yolo_model'].predict(image,
                                           conf=confidence,
                                           device=device,
                                           save=True if save else False,
                                           project=output_images_dir,
                                           name=run_name,
                                           save_txt=True if save_txt else False,
                                           exist_ok=True)

    result = results[0]
    print(result)
    im_array = result.plot()  # plot a BGR numpy array of predictions
    im_array = im_array[..., ::-1]
    im = Img.fromarray(im_array)  # RGB PIL image

    results = {
        "image": im,
        "image_size": {
            "height": im_array.shape[0],
            "width": im_array.shape[1],
            "channels": im_array.shape[2],
        },
        "boxes": result.boxes.xywhn.tolist()[0]
    }

    return results


def track(video_path: Optional[str],
          save=True,
          save_txt=True):  # path to img or url
    run_name = 'track'

    result = models['yolo_model'].track(source=video_path,
                                        conf=confidence,
                                        device=device,
                                        save=True,
                                        project=output_images_dir,
                                        name=run_name,
                                        save_txt=True,
                                        exist_ok=True)

    results = {
        'video_save_path': output_images_dir + '/' + run_name + '/' + video_path,
        'result': result
    }

    return results


