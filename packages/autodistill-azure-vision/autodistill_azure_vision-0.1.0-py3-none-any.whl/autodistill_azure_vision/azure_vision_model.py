import os
from dataclasses import dataclass

import numpy as np
import requests
import supervision as sv
from autodistill.detection import CaptionOntology, DetectionBaseModel

HOME = os.path.expanduser("~")


@dataclass
class AzureVision(DetectionBaseModel):
    ontology: CaptionOntology

    def __init__(self, ontology: CaptionOntology, endpoint: str, subscription_key: str):
        self.ontology = ontology
        self.endpoint = endpoint
        self.subscription_key = subscription_key
        pass

    def predict(self, input: str, confidence: int = 0.5) -> sv.Detections:
        image = open(input, "rb").read()

        self.headers = {
            "Content-Type": "application/octet-stream",
            "Ocp-Apim-Subscription-Key": self.subscription_key,
        }

        response = requests.post(self.endpoint, headers=self.headers, data=image).json()

        xyxys, confidences, class_ids = [], [], []

        classes = self.ontology.classes()

        for detection in response["objectsResult"]["values"]:
            bbox = detection["boundingBox"]

            tags = detection["tags"]

            x0 = bbox["x"]
            y0 = bbox["y"]
            x1 = x0 + bbox["w"]
            y1 = y0 + bbox["h"]

            for tag in tags:
                if tag["confidence"] < confidence:
                    continue

                if tag["name"] not in classes:
                    continue

                xyxys.append([x0, y0, x1, y1])
                confidences.append(tag["confidence"])
                class_ids.append(classes.index(tag["name"]))

        if len(xyxys) == 0:
            return sv.Detections.empty()

        return sv.Detections(
            xyxy=np.array(xyxys),
            class_id=np.array(class_ids),
            confidence=np.array(confidences),
        )
