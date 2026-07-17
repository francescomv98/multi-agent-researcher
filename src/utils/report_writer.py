from pathlib import Path

class ReportWriter:

    def __init__(self, output_path: str):
        self.output_path = Path(output_path)

    def save(self, content: str):

        self.output_path.parent.mkdir(parents=True, exist_ok=True)

        self.output_path.write_text(content, encoding="utf-8")