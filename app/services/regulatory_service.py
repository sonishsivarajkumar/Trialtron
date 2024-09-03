# app/services/regulatory_service.py
class RegulatoryService:
    @staticmethod
    def check_compliance(document_content: str):
        # Implement regulatory compliance checking logic here
        # This is a placeholder and should be replaced with actual compliance checking
        compliance_issues = []
        if "safety data" not in document_content.lower():
            compliance_issues.append("Missing safety data section")
        if "efficacy results" not in document_content.lower():
            compliance_issues.append("Missing efficacy results")
        return compliance_issues