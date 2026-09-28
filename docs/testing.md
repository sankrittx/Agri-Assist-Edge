# Testing Plan

## Hardware tests

- [ ] Soil-moisture sensor calibration
- [ ] DHT22 reading stability
- [ ] LCD communication
- [ ] Relay switching
- [ ] Pump operation
- [ ] ESP32-CAM image capture
- [ ] ESP32-CAM Wi-Fi transmission
- [ ] Arduino/Raspberry Pi serial communication
- [ ] Power stability under pump load

## AI tests

- [ ] Dataset split
- [ ] Training validation
- [ ] Held-out test set
- [ ] Confusion matrix
- [ ] Precision/recall/F1
- [ ] Raspberry Pi latency benchmark
- [ ] Low-light image testing
- [ ] Field image testing

## System tests

- [ ] Dry soil → irrigation decision
- [ ] Wet soil → pump remains OFF
- [ ] Low-confidence AI result → uncertainty warning
- [ ] Pump command reaches Arduino
- [ ] Relay switches correctly
- [ ] LCD reflects current state
- [ ] Recovery after Wi-Fi interruption
- [ ] Recovery after Raspberry Pi restart
