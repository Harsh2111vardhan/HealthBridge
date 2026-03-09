def run_doctor_agent(data):
    """
    Doctor Agent:
    Performs simple clinical reasoning based on patient symptoms.
    Returns possible conditions and a severity signal.
    """

    symptoms = [s.lower() for s in data.get("symptoms", [])]

    conditions = []
    severity_signal = 0.3

    # Malaria pattern
    if "fever" in symptoms and "body_pain" in symptoms:
        conditions.append({
            "name": "malaria",
            "probability": 0.45
        })
        severity_signal += 0.2

    # Typhoid pattern
    if "fever" in symptoms and "headache" in symptoms:
        conditions.append({
            "name": "typhoid",
            "probability": 0.30
        })
        severity_signal += 0.2

    # Pneumonia pattern
    if "cough" in symptoms and "fever" in symptoms:
        conditions.append({
            "name": "pneumonia",
            "probability": 0.40
        })
        severity_signal += 0.3

    # Gastroenteritis pattern
    if "abdominal_pain" in symptoms and "diarrhea" in symptoms:
        conditions.append({
            "name": "gastroenteritis",
            "probability": 0.50
        })
        severity_signal += 0.2

    # If no pattern matched
    if not conditions:
        conditions.append({
            "name": "general_infection",
            "probability": 0.20
        })

    # Cap severity between 0 and 1
    severity_signal = min(severity_signal, 1.0)

    return {
        "conditions": conditions,
        "severity_signal": severity_signal
    }