# Security

## Do not commit secrets

Never commit:

- passwords
- API keys
- Wi-Fi credentials
- cloud credentials
- private certificates

Use environment variables or local configuration.

## Hardware safety

The pump is an electrically powered actuator. Use a correctly rated relay, power supply and wiring. Never power the pump directly from a microcontroller GPIO.

## Data

If field data containing identifiable information is collected, obtain appropriate consent and avoid publishing raw personal data in this repository.
