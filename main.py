from image_processing import ImageProcessor
import cv2
from dotenv import load_dotenv

from roboflow import Roboflow
import supervision as sv
import time
import os

load_dotenv()

# ENV Variables

camera_login = os.getenv("CAMERA_LOGIN")
camera_pass = os.getenv("CAMERA_PASSWORD")
camera_address = os.getenv("CAMERA_ADDRESS")
roboflow_key = os.getenv("ROBOFLOW_KEY")

# Services

image_processor = ImageProcessor(roboflow_key=roboflow_key)

# Methods

def start(demo):
    vcap = cv2.VideoCapture(f"rtsp://{camera_login}:{camera_pass}@{camera_address}")
    while(1):
        ret, frame = vcap.read()
        # frame = cv2.imread('processed_images/test_1.png')
        
        result = image_processor.process_image(frame)
        
        if demo:
            cv2.imshow('VIDEO', result.annotated_image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            time.sleep(20)

start(demo=False)