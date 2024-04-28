from image_processing import ImageProcessor
import cv2
from dotenv import load_dotenv

import time
import os
from weights_version import WeightsVersion

load_dotenv()

# ENV Variables

camera_login = os.getenv("CAMERA_LOGIN")
camera_pass = os.getenv("CAMERA_PASSWORD")
camera_address = os.getenv("CAMERA_ADDRESS")
yolo_repo_path = os.getenv("YOLO_REPO_PATH")

# Services

image_processor = ImageProcessor(weights=WeightsVersion.MARK_1, yolo_repo_path=yolo_repo_path)

# Methods

def start(demo):
    vcap = cv2.VideoCapture(f"rtsp://{camera_login}:{camera_pass}@{camera_address}")
    while(1):
        ret, frame = vcap.read()
        # frame = cv2.imread('processed_images/test_1.png')
        
        result = image_processor.process_image(frame)
        print(result)
        
        if demo:
            cv2.imshow('VIDEO', result.annotated_image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            time.sleep(20)

start(demo=False)