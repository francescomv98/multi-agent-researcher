from pydantic import BaseModel
from typing import List

class ReportSection(BaseModel):
    title: str
    content: str

class ResearchReport(BaseModel):
    title: str
    executive_summary: str
    sections: List[ReportSection]
    conclusion: str