# app/services/regulatory_service.py
import re

class RegulatoryService:
    def __init__(self):
        self.compliance_rules = [
            (r'\b(?:confidential|private)\b', "Contains confidential information"),
            (r'\b(?:not approved|unapproved)\b', "References unapproved claims"),
            (r'\b(?:guarantee|promise)\b', "Contains guarantee or promise statements"),
        ]

    def check_compliance(self, content):
        issues = []
        for pattern, issue in self.compliance_rules:
            if re.search(pattern, content, re.IGNORECASE):
                issues.append(issue)
        return issues