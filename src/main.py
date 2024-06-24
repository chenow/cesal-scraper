# noqa: INP001
from logging import getLogger

from cesal_scraper import HousingAvailabilityChecker, setup_logging

LOGGER = getLogger(__name__)


def main() -> None:
    LOGGER.info("Checking housing availability...")
    checker = HousingAvailabilityChecker()
    checker.check_availability()


if __name__ == "__main__":
    setup_logging()
    main()
