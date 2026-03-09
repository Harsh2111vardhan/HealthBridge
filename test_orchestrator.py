from backend.app.orchestrator import Orchestrator

# Create orchestrator instance
orchestrator = Orchestrator()

# Sample patient input
patient_input = {
    "symptoms": ["fever", "body_pain"],
    "medications": ["Brufen", "Aspirin"],
    "conditions": []
}

# Run full pipeline
result = orchestrator.run_pipeline(patient_input)

print("Pipeline Output:")
print(result)