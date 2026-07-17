from crew import ResearchCrew
from src.utils.report_writer import ReportWriter
from src.utils.logger import setup_logger

logger = setup_logger()

def main():

    logger = setup_logger()

    topic = input("Research topic: ")

    logger.info(f"Starting research for topic: {topic}")

    result = ResearchCrew().crew().kickoff(
        inputs={
            "topic": topic
        }
    )

    logger.info("Crew execution completed")

    writer = ReportWriter("output/reports/final_report.md")
    writer.save(result.raw)

    logger.info("Report saved successfully")

if __name__ == "__main__":
    main()