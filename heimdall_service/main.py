from image_processing import ImageProcessor
from dotenv import load_dotenv

import os
from weights_version import WeightsVersion
from GatewayService import GatewayService
from VisionServiceRuntime import VisionServiceRuntime
from DescriptionService import DescriptionService
from application import Application

load_dotenv()

# ENV Variables

camera_login = os.getenv("CAMERA_LOGIN")
camera_pass = os.getenv("CAMERA_PASSWORD")
camera_address = os.getenv("CAMERA_ADDRESS")
yolo_repo_path = os.getenv("YOLO_REPO_PATH")

llm_service_url = os.getenv("LLM_SERVICE_URL")
llm_auth_token = os.getenv("LLM_AUTH_TOKEN")

# Methods

if __name__ == '__main__':
    image_processor = ImageProcessor(weights=WeightsVersion.MARK_2, yolo_repo_path=yolo_repo_path)
    vision_service_runtime = VisionServiceRuntime(camera_login, camera_pass, camera_address, image_processor)
    description_service = DescriptionService(llm_service_url, llm_auth_token)
    gateway_service = GatewayService(vision_service_runtime, description_service)

    app = Application(gateway_service, vision_service_runtime)
    app.run_app()
