import io
import os
from dataclasses import dataclass

import boto3
import numpy as np
import supervision as sv
from autodistill.detection import CaptionOntology, DetectionBaseModel
from PIL import Image

HOME = os.path.expanduser("~")


@dataclass
class Rekognition(DetectionBaseModel):
    ontology: CaptionOntology

    def __init__(self, ontology: CaptionOntology):
        self.ontology = ontology
        self.session = boto3.Session()
        self.client = self.session.client("rekognition")

        pass

    def predict(self, input: str, confidence: int = 0.5) -> sv.Detections:
        classes = self.ontology.classes()

        with Image.open(input) as image:
            buffered = io.BytesIO()
            image.save(buffered, format=image.format)
            image_bytes = buffered.getvalue()

        response = self.client.detect_labels(Image={"Bytes": image_bytes})

        xyxys, confidences, class_ids = [], [], []

        for label in response["Labels"]:
            if len(label["Instances"]) == 0:
                continue

            for box in label["Instances"]:
                if label["Name"] not in classes:
                    continue

                x0 = box["BoundingBox"]["Left"]
                y0 = box["BoundingBox"]["Top"]
                x1 = x0 + box["BoundingBox"]["Width"]
                y1 = y0 + box["BoundingBox"]["Height"]
                xyxys.append([x0, y0, x1, y1])

                confidences.append(box["Confidence"])

                class_ids.append(classes.index(label["Name"]))

        if len(xyxys) == 0:
            return sv.Detections.empty()

        return sv.Detections(
            xyxy=np.array(xyxys),
            class_id=np.array(class_ids),
            confidence=np.array(confidences),
        )
