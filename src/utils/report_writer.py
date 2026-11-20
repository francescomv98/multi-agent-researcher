import re
from datetime import datetime
from pathlib import Path
from typing import Optional, Union

REPORTS_DIR = Path("output/reports")


def slugify(text: str, max_length: int = 50) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:max_length].rstrip("-") or "report"


def report_path_for(topic: str, when: Optional[datetime] = None) -> Path:
    when = when or datetime.now()
    return REPORTS_DIR / f"{when:%Y%m%d_%H%M%S}_{slugify(topic)}.md"


class ReportWriter:

    def __init__(self, output_path: Union[str, Path]):
        self.output_path = Path(output_path)

    def save(self, content: str) -> Path:
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        self.output_path.write_text(content, encoding="utf-8")
        return self.output_path
