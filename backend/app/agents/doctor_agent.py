def run_doctor_agent(data):

    symptoms = data.get("symptoms", [])

    return {
        "conditions": [
            {"name": "malaria", "probability": 0.45},
            {"name": "typhoid", "probability": 0.30}
        ],
        "severity_signal": 0.6
    }