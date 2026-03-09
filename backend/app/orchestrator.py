# Orchestrator module for coordinating agents

from backend.app.agents.intake_agent import run_intake_agent
from backend.app.agents.triage_agent import run_triage_agent
from backend.app.agents.diagnosis_agent import run_diagnosis_agent
from backend.app.agents.pharmacist_agent import run_pharmacist_agent


class Orchestrator:
    """Handles the orchestration of clinical agents."""

    def __init__(self):
        pass

    def run_pipeline(self, patient_input):
        """
        Runs the full clinical diagnosis pipeline.
        """

        # Step 1: Intake Agent
        intake_output = run_intake_agent(patient_input)

        # Step 2: Triage Agent
        triage_output = run_triage_agent(intake_output)

        # Step 3: Diagnosis Agent
        diagnosis_output = run_diagnosis_agent(intake_output)

        # Step 4: Pharmacist Agent
        pharmacist_output = run_pharmacist_agent(intake_output)

        # Combine results
        final_result = {
            "intake": intake_output,
            "triage": triage_output,
            "diagnosis": diagnosis_output,
            "medication_safety": pharmacist_output
        }

        return final_result