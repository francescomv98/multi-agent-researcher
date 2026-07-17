from src.models.report import ResearchReport

def validate_report(report_data: dict) -> ResearchReport:
    
    return ResearchReport(**report_data)