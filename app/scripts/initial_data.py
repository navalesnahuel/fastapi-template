import logging

from sqlmodel import Session

from ..database import engine, init_db

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",  # Simplified format
    datefmt="%Y-%m-%d %H:%M:%S",  # Custom date format
    level=logging.INFO,  # Set log level
)


logger = logging.getLogger(__name__)


def init() -> None:
    with Session(engine) as session:
        init_db(session)


def main() -> None:
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
