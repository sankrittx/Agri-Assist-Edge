# Contributing

Agri-Assist Edge is currently an academic prototype.

## Development flow

1. Create a feature branch.
2. Make one focused change.
3. Test the change on hardware or a reproducible simulator.
4. Update documentation.
5. Open a pull request.

Example:

```bash
git checkout -b feature/esp32-image-pipeline
git add .
git commit -m "Add ESP32-CAM image pipeline"
git push origin feature/esp32-image-pipeline
```

Never commit:

- Wi-Fi passwords
- API keys
- private datasets
- personal farmer data
- generated model secrets
- local `.env` files
