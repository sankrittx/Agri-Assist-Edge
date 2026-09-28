"""
Crop-health interpretation helpers.
"""


def interpret_prediction(class_name: str, confidence: float,
                          minimum_confidence: float = 0.70) -> dict:
    if confidence < minimum_confidence:
        return {
            "status": "uncertain",
            "class_name": class_name,
            "confidence": confidence,
            "warning": "AI confidence is below the validated threshold.",
        }

    if class_name.lower() == "healthy":
        return {
            "status": "healthy",
            "class_name": class_name,
            "confidence": confidence,
            "warning": None,
        }

    return {
        "status": "attention_required",
        "class_name": class_name,
        "confidence": confidence,
        "warning": "Crop-health condition requires review.",
    }
