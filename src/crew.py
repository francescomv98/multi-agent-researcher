from typing import List
from crewai import Agent, Crew, Process, Task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.project import CrewBase, agent, crew, task
from tools.search_tool import search_tool
from config.llm import get_llm
from config.settings import settings

@CrewBase
class ResearchCrew:
    """Multi-Agent Research Crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def planner(self) -> Agent:
        return Agent(
            config=self.agents_config["planner"],
            verbose=settings.verbose,
            llm=get_llm()
        )

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            verbose=settings.verbose,
            llm=get_llm(),
            tools=[search_tool]
        )

    @agent
    def summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config["summarizer"],
            verbose=settings.verbose,
            llm=get_llm()
        )

    @agent
    def reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config["reviewer"],
            verbose=settings.verbose,
            llm=get_llm()
        )


    @task
    def planning_task(self) -> Task:
        return Task(
            config=self.tasks_config["planning_task"],
            agent=self.planner()
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_task"],
            agent=self.researcher(),
            context=[self.planning_task()]
        )

    @task
    def summary_task(self) -> Task:
        return Task(
            config=self.tasks_config["summary_task"],
            agent=self.summarizer(),
            context=[self.research_task()]
        )

    @task
    def review_task(self) -> Task:
        return Task(
            config=self.tasks_config["review_task"],
            agent=self.reviewer(),
            context=[self.summary_task()]
        )


    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=settings.verbose
        )