"""
Agri-Assist Edge inference interface.

This module intentionally separates model loading from the rest of the
application. Put the validated deployment model in ai/models/ and implement
the model-specific preprocessing/postprocessing here.

The current implementation provides a safe development stub so the rest of
the repository can be tested without pretending that a trained model exists.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class Prediction:
    class_name: str
    confidence: float
    model_version: str


class CropHealthModel:
    def __init__(self, model_path: Optional[str] = None):
        self.model_path = Path(model_path) if model_path else None

        if self.model_path and not self.model_path.exists():
            raise FileNotFoundError(f"Model not found: {self.model_path}")

    def predict(self, image_path: str) -> Prediction:
        """
        Replace this method with the validated TensorFlow Lite / ONNX /
        compatible inference implementation.

        The current version deliberately returns an 'unavailable' state
        rather than inventing a diagnosis.
        """
        return Prediction(
            class_name="inference_unavailable",
            confidence=0.0,
            model_version="development-stub",
        )


if __name__ == "__main__":
    model = CropHealthModel()
    print(model.predict("example.jpg"))
