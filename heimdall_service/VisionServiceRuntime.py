import cv2
import time

class VisionServiceRuntime:

    def __init__(self, camera_login, camera_pass, camera_address, image_processor, interval=20):
        self.camera_login = camera_login
        self.camera_pass = camera_pass
        self.camera_address = camera_address
        self.image_processor = image_processor
        self.interval = interval

    def start(self, demo):
        vcap = cv2.VideoCapture(f"rtsp://{self.camera_login}:{self.camera_pass}@{self.camera_address}")
        while True:
            ret, frame = vcap.read()

            if not ret:
                print("Failed to grab frame")
                break

            result = self.image_processor.process_image(frame)
            print(result)

            self.result = result
            if demo:
                cv2.imshow('VIDEO', result.annotated_image)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                time.sleep(self.interval)
