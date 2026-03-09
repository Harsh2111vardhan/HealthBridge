# Diagnosis Agent - Handles diagnostic assessment and recommendations

# class DiagnosisAgent:
#     """Agent responsible for generating diagnostic assessments based on patient data."""

#     def __init__(self):
#         self.name = "DiagnosisAgent"
#         self.diagnoses = []
#         self.confidence_threshold = 0.6

#     def generate_diagnosis(self, patient_data):
#         """Generate diagnostic assessment based on patient symptoms and history."""
#         if not patient_data:
#             raise ValueError("Patient data cannot be empty")
        
#         chief_complaint = patient_data.get("chief_complaint", "")
#         medical_history = patient_data.get("medical_history", [])
#         symptoms = patient_data.get("symptoms", [])
        
#         # Analyze symptoms and history
#         possible_diagnoses = self._analyze_symptoms(chief_complaint, symptoms, medical_history)
        
#         diagnosis_result = {
#             "patient_id": patient_data.get("patient_id"),
#             "chief_complaint": chief_complaint,
#             "possible_diagnoses": possible_diagnoses,
#             "recommended_tests": self._recommend_tests(possible_diagnoses),
#             "confidence_score": self._calculate_confidence(possible_diagnoses)
#         }
        
#         self.diagnoses.append(diagnosis_result)
#         return diagnosis_result

#     def _analyze_symptoms(self, chief_complaint, symptoms, medical_history):
#         """Analyze symptoms and medical history to determine possible diagnoses."""
#         possible_diagnoses = []
        
#         # Simple symptom-to-diagnosis mapping
#         symptom_diagnosis_map = {
#             "fever": "Infection/Fever",
#             "cough": "Respiratory Infection",
#             "headache": "Migraine/Tension Headache",
#             "chest pain": "Cardiac/Pulmonary Issue",
#             "shortness of breath": "Respiratory Condition",
#             "nausea": "Gastrointestinal Issue",
#             "fatigue": "Anemia/Chronic Condition"
#         }
        
#         complaint_lower = chief_complaint.lower()
#         for symptom, diagnosis in symptom_diagnosis_map.items():
#             if symptom in complaint_lower:
#                 possible_diagnoses.append(diagnosis)
        
#         # Check medical history for related conditions
#         if medical_history:
#             possible_diagnoses.extend(medical_history)
        
#         return list(set(possible_diagnoses)) if possible_diagnoses else ["Awaiting further evaluation"]

#     def _recommend_tests(self, diagnoses):
#         """Recommend diagnostic tests based on possible diagnoses."""
#         test_map = {
#             "Infection/Fever": ["CBC", "Blood Culture", "Urinalysis"],
#             "Respiratory Infection": ["Chest X-ray", "Throat Culture", "Spirometry"],
#             "Cardiac/Pulmonary Issue": ["ECG", "Chest X-ray", "Troponin Test"],
#             "Gastrointestinal Issue": ["Abdominal Ultrasound", "Endoscopy", "Stool Test"],
#             "Anemia/Chronic Condition": ["CBC", "Iron Panel", "Metabolic Panel"]
#         }
        
#         recommended = set()
#         for diagnosis in diagnoses:
#             if diagnosis in test_map:
#                 recommended.update(test_map[diagnosis])
        
#         return list(recommended) if recommended else ["Clinical Evaluation"]

#     def _calculate_confidence(self, diagnoses):
#         """Calculate confidence score for the diagnostic assessment."""
#         # Simple confidence based on number of matching symptoms
#         base_confidence = 0.5 + (len(diagnoses) * 0.1)
#         return min(base_confidence, 0.95)  # Cap at 0.95

#     def get_diagnosis_history(self):
#         """Return the history of diagnostic assessments."""
#         return self.diagnoses 

def run_diagnosis_agent(data):
    """
    Simple diagnosis placeholder.
    """

    symptoms = data.get("symptoms", [])

    if "fever" in symptoms and "body_pain" in symptoms:
        diagnosis = ["viral_fever"]
    else:
        diagnosis = ["general_checkup"]

    return {
        "possible_diagnosis": diagnosis
    }