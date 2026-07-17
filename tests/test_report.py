from src.models.report import ResearchReport, ReportSection

def test_report_creation():

    report = ResearchReport(
        title="Test Report",
        executive_summary="Summary",
        sections=[
            ReportSection(
                title="Section 1",
                content="Content"
            )
        ],
        conclusion="Conclusion"
    )

    assert report.title == "Test Report"
    assert len(report.sections) == 1
    assert report.sections[0].title == "Section 1"