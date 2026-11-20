from pathlib import Path
from typing import Callable, Optional

from src.crew import ResearchCrew
from src.utils.report_writer import REPORTS_DIR, ReportWriter, report_path_for


def run_research(topic: str, on_task_done: Optional[Callable] = None) -> Path:
    topic = topic.strip()
    if not topic:
        raise ValueError("Research topic cannot be empty")

    crew = ResearchCrew().crew()
    if on_task_done:
        crew.task_callback = on_task_done

    result = crew.kickoff(inputs={"topic": topic})

    if not result.raw or not result.raw.strip():
        raise RuntimeError("The crew finished but returned an empty report")

    path = report_path_for(topic)
    ReportWriter(path).save(result.raw)
    return path
