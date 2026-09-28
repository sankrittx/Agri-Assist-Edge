# AI Inference

Place the validated deployment model under:

```text
ai/models/
```

The model should expose a prediction interface returning:

- class name
- confidence
- model version

The current `inference.py` contains a development stub. It does not claim to detect disease until a trained and validated model is integrated.
