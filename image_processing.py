import cv2
from dotenv import load_dotenv

load_dotenv()
import os

camera_login = os.getenv("CAMERA_LOGIN")
camera_pass = os.getenv("CAMERA_PASSWORD")
camera_address = os.getenv("CAMERA_ADDRESS")

def retrieve_image():
    vcap = cv2.VideoCapture(f"rtsp://{camera_login}:{camera_pass}@{camera_address}")
    while(1):
        ret, frame = vcap.read()
        cv2.imshow('VIDEO', frame)
        cv2.waitKey(1)
    # ret, frame = vcap.read()
    # process_image(frame)

def process_image(image): 
    print("Processing image...")
    return "Image processed"

retrieve_image()

