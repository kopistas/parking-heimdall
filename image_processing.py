import supervision as sv
import cv2
import numpy as np
import torch
from weights_version import WeightsVersion
import os

class ImageProcessingResult:

    annotated_image: np.array

    def __init__(self, total, occupied_count, empty_count, annotated_image):
        self.total = total
        self.occupied_count = occupied_count
        self.empty_count = empty_count
        self.annotated_image = annotated_image

    def __repr__(self) -> str:
        return f"Detected places:\nFree: {self.empty_count}\nOccupied: {self.occupied_count}\nTotal:{self.total}"

class ImageProcessor:

    last_result: ImageProcessingResult
    model: any

    def __init__(self, weights: WeightsVersion, yolo_repo_path=str):
        current_file_directory = os.path.dirname(os.path.abspath(__file__))
        path = f"{current_file_directory}/weights/{weights.value}.pt"
        self.model = torch.hub.load(yolo_repo_path, 'custom', path=path, source='local')

    def process_image(self, image) -> ImageProcessingResult:
        results = self.model(image)

        detected_objects = results.xyxy[0] 
        
        names = self.model.module.names if hasattr(self.model, 'module') else self.model.names

        inv_names = {v: k for k, v in names.items()}

        occupied_idx = inv_names['occupied']
        free_idx = inv_names['free']

        occupied_count = (detected_objects[:, -1] == occupied_idx).sum().item()
        free_count = (detected_objects[:, -1] == free_idx).sum().item()

        annotated_image = np.squeeze(results.render())

        total_count = occupied_count + free_count
        return ImageProcessingResult(total_count, occupied_count, free_count, annotated_image)