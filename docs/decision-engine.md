# Decision Engine

The decision engine is responsible for converting sensor state and AI output into an actionable system state.

## Inputs

- Soil moisture
- Temperature
- Relative humidity
- Crop-health class
- AI confidence
- Optional future weather data
- Optional future farm history

## Example logic

```text
IF soil is dry
    AND AI confidence is low OR crop appears healthy:
        irrigation may be required

IF soil is sufficiently wet:
        pump OFF

IF disease/pest confidence exceeds validated threshold:
        generate crop-health warning

IF AI confidence is below validated threshold:
        mark result as uncertain
```

The exact thresholds must be calibrated against the target crop, soil and field conditions.

## Output

```json
{
  "pump": "ON",
  "irrigation_reason": "soil_moisture_low",
  "crop_health": "healthy",
  "confidence": 0.94,
  "warning": null
}
```

The engine should be treated as a decision-support component until field validation is complete.
