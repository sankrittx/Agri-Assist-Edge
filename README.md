# Agri-Assist Edge

**A locally operating, edge-AI smart farming assistant that combines crop vision, field sensors and environmental data to detect agricultural threats, make irrigation and risk decisions, and deliver actionable farmer advisories.**

Team **POTHAR** | Smart India Hackathon 2026 | Problem Statement **SIH26180** (Qualcomm Inc, Hardware, Agriculture)

> **Project status:** Under development. Design and documentation phase complete. Prototype build is in progress. See the [Roadmap](#roadmap).

---

## Problem

Farmers in remote areas lose yield to crop diseases, pests, nutrient problems, poor irrigation timing and extreme weather (drought, heat waves, floods). Most smart-farming tools depend on stable internet and cloud services, which are often unavailable in the field.

## Our solution

Agri-Assist Edge processes the important intelligence **on the device**, in the field, without needing the cloud for core decisions.

```
SENSE  ->  ANALYZE LOCALLY  ->  DECIDE  ->  ACT / ALERT
```

It turns crop images, sensor readings and weather data into simple decisions:

- Irrigate now / delay irrigation
- Possible disease detected
- Pest activity increasing
- Heat-stress warning
- Flood-risk alert

## Key features

- **On-device AI inference.** Works offline, cloud is not required for core intelligence
- **Crop disease detection** from leaf images
- **Pest detection** with location, class and confidence
- **Nutrient-deficiency indication** using image plus crop/environment context
- **Sensor-based irrigation decisions** with automatic pump control
- **Environmental risk alerts** for drought, heat and excess rain / flood risk
- **Farmer-friendly advisories** through LCD, mobile/web interface or SMS
- **Local data storage and dashboard**

## System architecture

```
                 CROP IMAGE (ESP32-CAM)
                          |
              +-----------+-----------+
              v                       v
         Disease AI               Pest AI
              |                       |
              +-----------+-----------+
                          v
                    AI OBSERVATIONS
                          |
Field sensors ------------+------------ Weather data
                          v
                   DECISION ENGINE
                          |
          +---------------+---------------+
          v               v               v
     Irrigation      Crop / Pest        Risk
      Decision        Advisory       Assessment
          |               |               |
          +---------------+---------------+
                          v
                   FARMER ADVISORY
```

The AI models produce **observations**. The decision engine combines those observations with sensor and environmental data to produce the final advice. Not every problem is forced into a deep-learning model.

> Add your diagram image here: `docs/architecture.png`

## Hardware

| Layer | Component |
|---|---|
| Soil / environment sensing | Arduino UNO R4 Minima + capacitive soil-moisture sensor + DHT22 (temperature and humidity) |
| Camera | ESP32-CAM |
| Edge computer | Raspberry Pi 5-class |
| AI acceleration | Raspberry Pi AI HAT+ (if required, to be evaluated) |
| Actuation | 5 V relay module + DC water pump |
| Farmer interface | 20x4 LCD, mobile/web interface, SMS (phased) |

**Roles**

- **Arduino UNO R4 Minima** reads sensors, drives the relay and pump, and shows status on the LCD
- **ESP32-CAM** captures crop/leaf images and sends them to the edge computer. It does not run the heavy AI model
- **Raspberry Pi** handles preprocessing, AI inference, sensor-data processing, risk analysis, the decision engine, local storage and the farmer backend

## AI and decision modules

| Module | Approach | Notes |
|---|---|---|
| Disease / crop health | Lightweight CNN (MobileNetV3 / EfficientNet-Lite candidates) | Classification with confidence score |
| Pest detection | Lightweight YOLO (YOLOv8n / YOLO11n-class candidates) | Object detection. Final version chosen after testing on target hardware and dataset |
| Nutrient deficiency | Image-based visual assessment + crop/environment context | Framed as an *indication*, not a confirmed diagnosis, until validated |
| Irrigation | Rule-based engine on soil moisture, temperature, humidity and weather | Outputs Irrigate / Delay / Stop |
| Environmental risk | Multivariate risk engine | Outputs drought, heat, excess-rain and flood-risk levels |

## Tech stack

- Python (inference, decision engine, backend)
- TensorFlow Lite / PyTorch / ONNX (edge inference, final choice after benchmarking)
- Arduino C++ (sensor and pump control)
- SQLite (local storage)
- Web dashboard (lightweight)

> Update this list to match what you actually end up using.

## Roadmap

- [x] Problem analysis and solution design
- [x] System architecture and hardware selection
- [x] Sensor + relay + pump prototype (Arduino)
- [ ] ESP32-CAM image capture pipeline
- [ ] Dataset collection and model training / benchmarking
- [ ] Edge deployment on Raspberry Pi
- [ ] Decision engine and risk engine
- [ ] Farmer interface (LCD, then web / SMS)
- [ ] Field testing and demo video

## Repository structure

```
agri-assist-edge/
├── README.md
├── docs/            # architecture diagram, flowcharts, project report
├── hardware/        # components list, circuit diagrams, BOM
├── firmware/        # Arduino / ESP32 code (coming soon)
├── edge/            # Raspberry Pi inference + decision engine (coming soon)
└── models/          # trained models (coming soon)
```

## Team POTHAR

- Sankrit Kashyap Saikia (Team Leader)
- Nandita Saikia
- Rashmi Priya Dangaria
- Prachurjya Singh
- Dhritikamal Das
- Sarfraz Mazid

## License

MIT License
