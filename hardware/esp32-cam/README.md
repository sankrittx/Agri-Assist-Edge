# ESP32-CAM

The ESP32-CAM provides crop/leaf images to the Raspberry Pi over Wi-Fi.

## Configuration

Edit:

```cpp
const char* WIFI_SSID = "YOUR_WIFI_SSID";
const char* WIFI_PASSWORD = "YOUR_WIFI_PASSWORD";
```

Do not commit real Wi-Fi credentials.

## Capture endpoint

After the ESP32-CAM starts, use:

```text
http://<ESP32-CAM-IP>/capture
```

The Raspberry Pi can periodically request this endpoint.

The exact camera pin mapping must match the ESP32-CAM board variant.
