# Hardware

## Bill of Materials

| Component | Qty | Approx. cost |
|---|---:|---:|
| Raspberry Pi 5 4GB | 1 | ₹13,400 |
| Raspberry Pi AI HAT+ 13 TOPS *(optional)* | 1 | ₹7,500 |
| Arduino UNO R4 Minima | 1 | ₹2,300 |
| ESP32-CAM + OV2640 | 1 | ₹750 |
| Capacitive soil-moisture sensor | 1 | ₹120 |
| DHT22 | 1 | ₹105 |
| 5V 1-channel relay | 1 | ₹45 |
| DC 3–6V mini pump | 1 | ₹50 |
| 20x4 I2C LCD | 1 | ₹335 |
| Supporting parts | - | ₹1,500 |

Base estimate: **₹18,600**

With optional AI HAT+: **₹26,100**

## Arduino pin plan

| Signal | Pin |
|---|---|
| Soil moisture analog output | A0 |
| DHT22 data | D2 |
| Relay input | D7 |
| LCD | SDA/SCL |

These are provisional values.

## Power

The pump must have its own appropriately rated supply. The relay isolates the pump load from the Arduino control signal.

The Raspberry Pi requires a dedicated USB-C supply. The ESP32-CAM requires a stable supply to avoid brownout/reset problems.

## Safety

Never connect the pump directly to an Arduino GPIO.

Never connect a 3–6V pump directly to a 12V supply.
