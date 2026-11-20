from src.research import run_research
from src.utils.logger import setup_logger


def main():
    logger = setup_logger()

    try:
        topic = input("Research topic: ").strip()
        logger.info(f"Starting research for topic: {topic}")

        report_path = run_research(topic)

        logger.info(f"Report saved to {report_path}")

    except ValueError as e:
        logger.error(f"Validation error: {e}")
    except Exception:
        logger.exception("Crew execution failed")


if __name__ == "__main__":
    main()
