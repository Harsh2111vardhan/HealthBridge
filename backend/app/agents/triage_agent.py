# Triage Agent - Handles patient triage and priority assessment

# class TriageAgent:
#     """Agent responsible for triaging patients and assessing priority levels."""

#     def __init__(self):
#         self.name = "TriageAgent"
#         self.triage_results = []
#         self.priority_levels = ["Critical", "High", "Medium", "Low"]

#     def assess_priority(self, patient_data):
#         """Assess the priority level of a patient based on intake data."""
#         if not patient_data:
#             raise ValueError("Patient data cannot be empty")
        
#         priority = self._calculate_priority(patient_data)
        
#         triage_result = {
#             "patient_id": patient_data.get("patient_id"),
#             "priority_level": priority,
#             "reason": self._get_priority_reason(priority, patient_data),
#             "recommended_department": self._recommend_department(priority)
#         }
        
#         self.triage_results.append(triage_result)
#         return triage_result

#     def _calculate_priority(self, patient_data):
#         """Calculate priority based on patient symptoms and conditions."""
#         chief_complaint = patient_data.get("chief_complaint", "").lower()
        
#         # Keywords indicating critical conditions
#         critical_keywords = ["chest pain", "difficulty breathing", "severe bleeding", "unconscious"]
#         if any(keyword in chief_complaint for keyword in critical_keywords):
#             return "Critical"
        
#         # Keywords indicating high priority
#         high_keywords = ["severe", "acute", "emergency", "trauma"]
#         if any(keyword in chief_complaint for keyword in high_keywords):
#             return "High"
        
#         # Keywords indicating medium priority
#         medium_keywords = ["moderate", "persistent", "concerning"]
#         if any(keyword in chief_complaint for keyword in medium_keywords):
#             return "Medium"
        
#         return "Low"

#     def _get_priority_reason(self, priority, patient_data):
#         """Generate a reason for the assigned priority."""
#         reasons = {
#             "Critical": "Life-threatening condition requiring immediate intervention",
#             "High": "Serious condition requiring urgent attention",
#             "Medium": "Condition requiring timely evaluation",
#             "Low": "Minor condition, routine scheduling appropriate"
#         }
#         return reasons.get(priority, "Unknown")

#     def _recommend_department(self, priority):
#         """Recommend the appropriate department based on priority."""
#         department_map = {
#             "Critical": "Emergency",
#             "High": "Urgent Care",
#             "Medium": "General Clinic",
#             "Low": "General Practice"
#         }
#         return department_map.get(priority, "General")

#     def get_triage_history(self):
#         """Return the history of triage assessments."""
#         return self.triage_results

def run_triage_agent(data):
    """
    Simple triage logic.
    """

    symptoms = data.get("symptoms", [])

    if "chest_pain" in symptoms:
        priority = "emergency"
    elif "fever" in symptoms:
        priority = "medium"
    else:
        priority = "low"

    return {
        "triage_level": priority
    }