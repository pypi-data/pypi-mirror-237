FROM python:3.8

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
COPY yolov8x.pt /yolov8x.pt
COPY requirements.txt /requirements.txt
COPY models/best.pt /models/best.pt
RUN pip install -r requirements.txt
COPY models/best_old.pt /models/best_old.pt
COPY image1.jpg /image1.jpg
COPY run.py /run.py

ENV PYTHONPATH "${PYTHONPATH}:/"

CMD uvicorn run:app --host=0.0.0.0 --port=8021
