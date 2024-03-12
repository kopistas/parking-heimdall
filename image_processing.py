from inference import get_model
# import supervision to visualize our results
import supervision as sv
# import cv2 to helo load our image
import cv2
import numpy as np

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

    def __init__(self, roboflow_key):
        self.roboflow_key = roboflow_key

    def process_image(self, image) -> ImageProcessingResult:
        # model = get_model(model_id="parking-spot-detector-a84ql/1", api_key=self.roboflow_key)
        model = get_model(model_id="parking-space-ipm1b/4", api_key=self.roboflow_key)
        results = model.infer(image)
        detections = sv.Detections.from_inference(results[0].dict(by_alias=True, exclude_none=True))
        total = len(detections.data["class_name"])
        occupied_count = np.count_nonzero(detections.data['class_name'] == 'occupied')
        empty_count = np.count_nonzero(detections.data['class_name'] == 'empty')

        # print(f"Detected places:\nFree: {empty_count}\nOccupied: {occupied_count}")

        bounding_box_annotator = sv.BoundingBoxAnnotator()
        label_annotator = sv.LabelAnnotator()

        annotated_image = bounding_box_annotator.annotate(
            scene=image, detections=detections)
        annotated_image = label_annotator.annotate(
            scene=annotated_image, detections=detections)
        cv2.imwrite("processed_images/last_annotated.png", annotated_image)
        result = ImageProcessingResult(total=total,
                                       occupied_count=occupied_count,
                                       empty_count=empty_count,
                                       annotated_image=annotated_image)
        self.last_result = result
        print(f"Result: {result}")
        # sv.plot_image(annotated_image)
        return result