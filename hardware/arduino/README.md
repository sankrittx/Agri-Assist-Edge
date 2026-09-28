# Arduino Controller

The Arduino handles low-level sensing and actuation.

## Required libraries

Install:

- `DHT sensor library`
- `LiquidCrystal I2C`

## Pin map

| Component | Pin |
|---|---|
| Soil moisture | A0 |
| DHT22 | D2 |
| Relay | D7 |
| LCD | SDA/SCL |

## Serial protocol

Commands:

```text
PUMP_ON
PUMP_OFF
```

Telemetry is emitted as JSON lines.

> Relay polarity and soil threshold must be verified on the actual hardware.
