# # import cv2
from PIL import Image as Img
# # from ultralytics import YOLO
# # import torch
# #
# #
# # device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# # models = {}
# # confidence = 0.5  # todo make config
# #
# #
# # models['yolo_model'] = YOLO('yolov8x.yaml')  # build a new model from scratch
# # models['yolo_model'] = YOLO('yolov8x.pt')  # load a pretrained model (recommended for training)
# # models['yolo_model'] = YOLO('models/best.pt')
# #
# #
# # image_path = 'image1.jpg'
# # # image_path = 'image3.png'
# # # image_path = '3173912184623786106.jpg'
# # video_path = 'vid3.mp4'
# # result = models['yolo_model'].predict(source=image_path,
# #                                       conf=confidence)
# #                                       # save=True,
# #                                       # project='results',
# #                                       # save_txt=True)
# #
# # # print(result)
# # run_name = 'track'
# # # result = models['yolo_model'].track(source=video_path,
# # #                                     conf=confidence,
# # #                                     save=True,
# # #                                     project=output_images_dir,
# # #                                     name=run_name,
# # #                                     save_txt=True)
# # # if True:
# # #     cap = cv2.VideoCapture(video_path)
# # #
# # #     # Loop through the video frames
# # #     while cap.isOpened():
# # #         # Read a frame from the video
# # #         success, frame = cap.read()
# # #
# # #         if success:
# # #             # Run YOLOv8 tracking on the frame, persisting tracks between frames
# # #             results = models["yolo_model"].track(frame, persist=True, imgsz=(720, 1280), tracker='botsort.yaml', conf=0.5, iou=0.5, agnostic_nms=True)
# # #
# # #             # Visualize the results on the frame
# # #             annotated_frame = results[0].plot()
# # #
# # #             # Display the annotated frame
# # #             cv2.imshow("YOLOv8 Tracking", annotated_frame)
# # #             cv2.waitKey(1)
# # #
# # # print(result[0])
# # # result[0].plot()
# # # import cv2
# # # # cv2.imshow('predicted_image', result[0].)
# # # cv2.waitKey(0)
# # # image = cv2.imread('results/predict13/' + image_path)
# # # cv2.imshow('predicted_image', image)
# # # cv2.waitKey(0)
# #
# # print(result[0].boxes.xywhn)
# #
# # for r in result:
# #     boxes = [detect.boxes.xywhn for detect in r]
# #     print(boxes)
# #     im_array = r.plot()  # plot a BGR numpy array of predictions
# #     print(type(im_array))
# #     im_array = im_array[..., ::-1]
# #     im = Img.fromarray(im_array)  # RGB PIL image
# #     print(type(im))
# #     res = im.tobytes()
# #     import numpy as np
# #     image_array = np.frombuffer(res, dtype=np.uint8).reshape(im_array.shape)
# #     im2 = Img.fromarray(image_array)
#     # im2.show()
#     # print(image_array)
#     # res2 = im_array.tobytes()
#     # import io
#     # tmp = io.BytesIO(res)
#     # tmp2 = io.BytesIO(res2)
#     # print(tmp)
#     # img_ = Img.open(tmp)
#     # print(img_)
#     # img_.show()  # show image
#     # im.show()  # show image
#     # im.save('results1.jpg')  # save image
#     # im.save('/Users/mikhail_korotkov/PycharmProjects/nike_detector/nike_detector/results1.jpg')
# import requests
# import base64
# import json
# import numpy as np
# # imm = Img.open("image1.jpg")
# # print(imm)
# # enc = base64.b64encode(imm)
# # json_data = json.dumps(np.array(imm).tolist())
# # print(json_data)
# with open("image1.jpg", "rb") as image_file:
#     enc = base64.b64encode(image_file.read())
# # print(enc)
# import json
# payload = {
#     "image": enc,
# }
# # data = json.dumps(payload)
# # print(data)
# response = requests.post('http://0.0.0.0:8021/predict/',
#                          data=payload,
#                          headers={"content-type": "application/json"})
# bin = response.json()['image_binary']
# height = response.json()['image_size']['height']
# width = response.json()['image_size']['width']
# channels = response.json()['image_size']['channels']
# boxes = response.json()['boxes']
# print(boxes)
# # # # print(enc)
# # dec = base64.b64decode(bin)
# # # print(im_array.shape)
# # import numpy as np
# # image_array = np.frombuffer(dec, dtype=np.uint8).reshape((height, width, channels))
# # # print(image_array)
# # im2 = Img.fromarray(image_array)
# # im2.show()
#
# # import base64
# # tt = base64.b64encode(res)
# #
# # print(tt)



# from nike_detector.service import init_nike_model, predict, track
#
# model = init_nike_model()
# imm = Img.open("image1.jpg")
# video = 'vid3.mp4'
# t = predict(imm)
# print(t)
# # t['image'].show()
# t2 = track(video, False, False)
# print(t2)


from nike_detector import init_nike_model, predict
