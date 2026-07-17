from crew import ResearchCrew
from src.utils.report_writer import ReportWriter
from src.utils.logger import setup_logger

logger = setup_logger()

def main():

    logger = setup_logger()
    
    try:
        topic = input("Research topic: ")

        if not topic.strip():
            raise ValueError("Research topic cannot be empty")

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
        
    except ValueError as e:
        logger.error(f"Validation error: {e}")
    except Exception as e:
        logger.exception("Crew execution failed")

if __name__ == "__main__":
    main()