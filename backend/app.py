from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify({
        "status": "ok",
        "service": "agri-assist-edge-backend",
    })


@app.post("/decision")
def decision():
    data = request.get_json(silent=True) or {}

    required = ["soil_moisture"]

    missing = [key for key in required if key not in data]

    if missing:
        return jsonify({
            "error": "missing_fields",
            "fields": missing,
        }), 400

    soil_moisture = int(data["soil_moisture"])
    dry_threshold = int(data.get("dry_threshold", 650))

    pump = "ON" if soil_moisture >= dry_threshold else "OFF"

    return jsonify({
        "soil_moisture": soil_moisture,
        "dry_threshold": dry_threshold,
        "pump": pump,
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
