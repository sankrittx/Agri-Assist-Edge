/*
 * Agri-Assist Edge
 * Arduino UNO R4 Minima - sensor and irrigation controller
 *
 * Provisional pin map:
 *   Soil moisture -> A0
 *   DHT22         -> D2
 *   Relay         -> D7
 *   LCD           -> SDA/SCL
 *
 * Serial commands from Raspberry Pi:
 *   PUMP_ON
 *   PUMP_OFF
 *
 * NOTE:
 * The soil threshold below is a starting point only.
 * Calibrate it for the actual sensor, soil and crop.
 */

#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <DHT.h>

#define SOIL_PIN A0
#define DHT_PIN 2
#define DHT_TYPE DHT22
#define RELAY_PIN 7

// Change to HIGH if your relay is active-high.
#define RELAY_ON LOW
#define RELAY_OFF HIGH

// Starting threshold; calibrate experimentally.
const int DRY_THRESHOLD = 650;

DHT dht(DHT_PIN, DHT_TYPE);
LiquidCrystal_I2C lcd(0x27, 20, 4);

unsigned long lastSensorRead = 0;
const unsigned long SENSOR_INTERVAL_MS = 2000;

void pumpOn() {
  digitalWrite(RELAY_PIN, RELAY_ON);
}

void pumpOff() {
  digitalWrite(RELAY_PIN, RELAY_OFF);
}

void updateLCD(int soil, float temp, float humidity) {
  lcd.clear();

  lcd.setCursor(0, 0);
  lcd.print("Soil: ");
  lcd.print(soil);

  lcd.setCursor(0, 1);
  lcd.print("Temp: ");
  if (isnan(temp)) lcd.print("ERR");
  else lcd.print(temp, 1);
  lcd.print(" C");

  lcd.setCursor(0, 2);
  lcd.print("Hum : ");
  if (isnan(humidity)) lcd.print("ERR");
  else lcd.print(humidity, 1);
  lcd.print(" %");

  lcd.setCursor(0, 3);
  lcd.print("Pump: ");
  lcd.print(digitalRead(RELAY_PIN) == RELAY_ON ? "ON" : "OFF");
}

void sendTelemetry() {
  int soil = analogRead(SOIL_PIN);
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  // Machine-readable telemetry for the Raspberry Pi.
  Serial.print("{\"soil_moisture\":");
  Serial.print(soil);
  Serial.print(",\"temperature\":");

  if (isnan(temperature)) Serial.print("null");
  else Serial.print(temperature, 2);

  Serial.print(",\"humidity\":");

  if (isnan(humidity)) Serial.print("null");
  else Serial.print(humidity, 2);

  Serial.print(",\"pump\":");
  Serial.print(digitalRead(RELAY_PIN) == RELAY_ON ? "\"ON\"" : "\"OFF\"");
  Serial.println("}");

  updateLCD(soil, temperature, humidity);
}

void handleCommand(String command) {
  command.trim();

  if (command == "PUMP_ON") {
    pumpOn();
    Serial.println("{\"ack\":\"PUMP_ON\"}");
  }
  else if (command == "PUMP_OFF") {
    pumpOff();
    Serial.println("{\"ack\":\"PUMP_OFF\"}");
  }
}

void setup() {
  Serial.begin(115200);

  pinMode(RELAY_PIN, OUTPUT);
  pumpOff();

  dht.begin();

  lcd.init();
  lcd.backlight();

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Agri-Assist Edge");
  lcd.setCursor(0, 1);
  lcd.print("Controller Ready");

  delay(1500);
}

void loop() {
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    handleCommand(command);
  }

  if (millis() - lastSensorRead >= SENSOR_INTERVAL_MS) {
    lastSensorRead = millis();
    sendTelemetry();
  }
}
