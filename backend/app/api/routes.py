from fastapi import APIRouter
from backend.app.agents.doctor_agent import run_doctor_agent
from backend.app.agents.radiology_lab_agent import run_radiology_agent
from backend.app.agents.pharmacist_agent import run_pharmacist_agent
from backend.app.agents.coordinator_agent import run_coordinator

router = APIRouter()

@router.post("/analyze")
def analyze_case(data: dict):

    doctor_output = run_doctor_agent(data)
    radiology_output = run_radiology_agent(data)
    pharmacist_output = run_pharmacist_agent(data)

    result = run_coordinator(
        doctor_output,
        radiology_output,
        pharmacist_output
    )

    return result