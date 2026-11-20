from datetime import datetime
from src.utils.report_writer import ReportWriter, report_path_for, slugify


def test_slugify():
    assert slugify("Renewable energy in Italy!") == "renewable-energy-in-italy"
    assert slugify("   ") == "report"
    assert len(slugify("a" * 200)) == 50


def test_report_path_is_unique_per_run():
    path = report_path_for("AI agents", datetime(2026, 1, 2, 3, 4, 5))
    assert path.name == "20260102_030405_ai-agents.md"


def test_writer_creates_folders(tmp_path):
    target = tmp_path / "nested" / "report.md"
    ReportWriter(target).save("# Hello")
    assert target.read_text(encoding="utf-8") == "# Hello"
