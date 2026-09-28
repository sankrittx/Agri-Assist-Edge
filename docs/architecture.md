# System Architecture

Agri-Assist Edge uses a two-level control architecture.

## High-level flow

```mermaid
flowchart LR
    CAM[ESP32-CAM] -->|Wi-Fi images| PI[Raspberry Pi 5]
    S[Soil Moisture] --> A[Arduino UNO R4 Minima]
    D[DHT22] --> A
    A -->|USB Serial| PI
    PI --> AI[Edge AI Inference]
    AI --> DE[Decision Engine]
    A <-->|Pump commands / telemetry| PI
    A --> R[Relay]
    R --> P[Water Pump]
    A --> LCD[20x4 I2C LCD]
```

## Design principle

- **Arduino:** deterministic low-level sensing and actuation.
- **ESP32-CAM:** image acquisition.
- **Raspberry Pi:** computation, AI inference and high-level decisions.
- **Decision Engine:** combines environmental state with AI output.
- **Relay/pump:** physical irrigation actuator.
- **LCD:** local farmer feedback.

The final physical architecture is also provided as `architecture.png`.
