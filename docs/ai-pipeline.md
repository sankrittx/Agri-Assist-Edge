# AI Pipeline

## Planned inference pipeline

```text
ESP32-CAM image
       ↓
Image validation
       ↓
Resize / normalization
       ↓
Edge AI model
       ↓
Predicted class + confidence
       ↓
Crop-health interpretation
       ↓
Decision Engine
```

## Model interface

The inference layer returns a standard result:

```json
{
  "class_name": "healthy",
  "confidence": 0.94,
  "model_version": "development"
}
```

The actual model is not committed until training and validation are complete.

## Model requirements

The deployed model should be evaluated for:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix
- Inference latency
- RAM usage
- Storage size
- Performance under real field lighting

## Edge deployment

The target is local inference on the Raspberry Pi. If benchmarking shows insufficient performance, an AI HAT+ may be evaluated.

Do not publish unsupported accuracy figures.
