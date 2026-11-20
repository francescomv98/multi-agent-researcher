import os

from crewai_tools import SerperDevTool

from src.config.settings import settings

# SerperDevTool reads the key straight from the environment, so make sure
# it's there even when it only lives in .env
os.environ.setdefault("SERPER_API_KEY", settings.serper_api_key)

search_tool = SerperDevTool()
