import pytest
from pydantic import ValidationError
from src.utils.validator import validate_report

def test_valid_report():

    data = {
        "title": "AI Research",
        "executive_summary": "Summary",
        "sections": [],
        "conclusion": "End"
    }

    report = validate_report(data)

    assert report.title == "AI Research"

def test_invalid_report():

    data = {
        "title": "AI Research"
    }

    with pytest.raises(ValidationError):
        validate_report(data)