import cv2
import os
import time
from dotenv import load_dotenv

load_dotenv()

camera_login = os.getenv("CAMERA_LOGIN")
camera_pass = os.getenv("CAMERA_PASSWORD")
camera_address = os.getenv("CAMERA_ADDRESS")


class ImageCollector:

    def __init__(self, login, password, address, save_folder):

        self.camera_url = f"rtsp://{login}:{password}@{address}"
        self.save_folder = save_folder
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
    
    def collect_images(self):
        vcap = cv2.VideoCapture(self.camera_url)
        while True:
            ret, frame = vcap.read()
            if ret:
                timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
                cv2.imwrite(f'{self.save_folder}/{timestamp}.png', frame)
                print(f'Image saved: {timestamp}.png')

                time.sleep(300) # Sleep for 5 minutes
            else:
                print('Error capturing image')
                break


image_collector = ImageCollector(camera_login, camera_pass, camera_address, "training_images")
image_collector.collect_images()