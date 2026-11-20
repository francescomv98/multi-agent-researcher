import os
from crewai_tools import SerperDevTool
from src.config.settings import settings

os.environ.setdefault("SERPER_API_KEY", settings.serper_api_key)

search_tool = SerperDevTool()
