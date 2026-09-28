"""
Agri-Assist Edge decision engine.

Run from the repository root:

python decision-engine/decision_engine.py \
  --soil-moisture 680 \
  --temperature 29 \
  --humidity 70 \
  --disease-class healthy \
  --disease-confidence 0.94
"""

import argparse
import json
import sys
from pathlib import Path

# Allow imports when executed directly from this directory.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from irrigation import irrigation_decision
from crop_health import interpret_prediction


def make_decision(
    soil_moisture: int,
    temperature: float | None,
    humidity: float | None,
    disease_class: str,
    disease_confidence: float,
    dry_threshold: int = 650,
) -> dict:

    irrigation = irrigation_decision(
        soil_moisture=soil_moisture,
        dry_threshold=dry_threshold,
    )

    health = interpret_prediction(
        class_name=disease_class,
        confidence=disease_confidence,
    )

    return {
        "sensor_data": {
            "soil_moisture": soil_moisture,
            "temperature": temperature,
            "humidity": humidity,
        },
        "crop_health": health,
        "irrigation": irrigation,
    }


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--soil-moisture", type=int, required=True)
    parser.add_argument("--temperature", type=float, default=None)
    parser.add_argument("--humidity", type=float, default=None)
    parser.add_argument("--disease-class", default="inference_unavailable")
    parser.add_argument("--disease-confidence", type=float, default=0.0)
    parser.add_argument("--dry-threshold", type=int, default=650)

    args = parser.parse_args()

    result = make_decision(
        soil_moisture=args.soil_moisture,
        temperature=args.temperature,
        humidity=args.humidity,
        disease_class=args.disease_class,
        disease_confidence=args.disease_confidence,
        dry_threshold=args.dry_threshold,
    )

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
