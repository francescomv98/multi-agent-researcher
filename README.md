# Multi-Agent Researcher

A multi-agent research system built with CrewAI that automatically plans, researches, summarizes and reviews complex topics using specialized AI agents. The project demonstrates an agentic AI workflow where multiple autonomous agents collaborate to transform a user research request into a structured professional report.

---

## Overview

Traditional research workflows require manually collecting information, organizing sources and writing summaries.
This project implements a multi-agent architecture where each agent has a specific responsibility in the research pipeline.
The system is composed of four specialized agents:

### Planner Agent

Responsible for understanding the user's research request and creating a structured investigation plan.
Responsibilities:
- Analyze the research topic.
- Break down the request into logical sections.
- Define the areas that need investigation.

---

### Researcher Agent

Responsible for collecting information following the research plan.
Responsibilities:
- Gather relevant information using external search capabilities.
- Organize findings by topic.
- Provide structured research notes.

---

### Summarizer Agent

Responsible for transforming research findings into a professional report.
Responsibilities:
- Create a structured Markdown document.
- Generate:
  - Title
  - Executive Summary
  - Main Sections
  - Conclusion

---

### Reviewer Agent

Responsible for reviewing and improving the final document.
Responsibilities:
- Check clarity.
- Improve consistency.
- Ensure readability and completeness.

---

## Architecture

The workflow follows a sequential multi-agent pipeline.

The execution flow is:

```text
User Research Topic
        |
        v
Planner Agent
        |
        v
Researcher Agent
        |
        v
Summarizer Agent
        |
        v
Reviewer Agent
        |
        v
Final Markdown Report
```

Each agent receives the output of the previous agent as context, creating a collaborative workflow where each component has a specific responsibility. The process is managed by CrewAI using a sequential execution strategy:

1. The Planner creates the research strategy.
2. The Researcher collects information using external tools.
3. The Summarizer transforms findings into a structured report.
4. The Reviewer improves the final document before delivery.

---

## Project Structure

The project is organized as follows:

```text
 multi-agent-researcher/
    ├── main.py
    ├── requirements.txt
    ├── README.md
    ├── .env
    │
    ├── src/
    │   ├── crew.py
    │   │
    │   ├── config/
    │   │   ├── agents.yaml
    │   │   ├── tasks.yaml
    │   │   ├── llm.py
    │   │   └── settings.py
    │   │
    │   ├── models/
    │   │   └── report.py
    │   │
    │   ├── tools/
    │   │   └── search_tool.py
    │   │
    │   └── utils/
    │       ├── logger.py
    │       ├── validator.py
    │       └── report_writer.py
    │
    ├── tests/
    │   ├── test_report.py
    │   └── test_validator.py
    │
    └── output/
        └── reports/
            └── final_report.md
```

## Technologies

The project is built using:

- Python 3.11
- CrewAI
- OpenAI API
- Pydantic
- Pytest
- Serper Search API
- YAML configuration files


## Installation

Clone the repository:
```bash
    git clone https://github.com/francescomv98/multi-agent-researcher.git
    cd multi-agent-researcher
```

Create a virtual environment: 
```bash
    python -m venv venv
```

Activate the virtual environment.

Windows:
```bash
    venv\Scripts\activate
```

Install dependencies:
```bash
    pip install -r requirements.txt
```


## Configuration

Create a `.env` file in the project root:
```bash
    MODEL_NAME=gpt-4.1-mini
    TEMPERATURE=0.2
    OPENAI_API_KEY=your_openai_api_key
    SERPER_API_KEY=your_serper_api_key
```

The application loads configuration values using `pydantic-settings`.
The `.env` file is excluded from version control.


## Running the Application

Start the application:
```bash
    python main.py
```

Insert a research topic:
    Research topic: Renewable energy in Italy

The system will execute the complete multi-agent workflow.

The final report will be generated at:
    output/reports/final_report.md


## Testing

The project includes automated tests covering:
- Report data models.
- Report validation logic.

Run tests with:
    pytest

Example result:
    2 passed


## Error Handling and Logging

The application includes:
- Crew execution error handling.
- Structured logging.
- Runtime execution tracking.

Logs are generated locally inside:
    logs/

The logs directory is excluded from version control.


## Report Validation

Generated reports are validated using Pydantic models before being written to disk.

The validation layer ensures that the final output respects the expected structure:
- Report title.
- Executive summary.
- Report sections.
- Conclusion.


## Purpose

This project was developed to explore:
- Agentic AI architectures.
- Multi-agent collaboration.
- LLM orchestration.
- Automated research workflows.
- AI-powered document generation.