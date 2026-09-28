"""
Irrigation decision logic.

Important:
The default threshold is only a development value. It must be calibrated
against the actual sensor and target crop/soil before field use.
"""


def irrigation_required(soil_moisture: int, dry_threshold: int = 650) -> bool:
    return soil_moisture >= dry_threshold


def irrigation_decision(
    soil_moisture: int,
    dry_threshold: int = 650,
) -> dict:
    required = irrigation_required(soil_moisture, dry_threshold)

    return {
        "pump": "ON" if required else "OFF",
        "reason": "soil_moisture_low" if required else "soil_moisture_sufficient",
    }
