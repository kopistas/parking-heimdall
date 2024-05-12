FROM python:3.8-slim

WORKDIR /usr/src/app

RUN apt-get update && \
    apt-get install -y git libgl1-mesa-glx libglib2.0-0 gcc python3-dev

COPY . .

RUN git clone https://github.com/ultralytics/yolov5

RUN pip install --no-cache-dir -r requirements.txt

ENV NAME World

CMD ["python", "./main.py"]
