# noqa: INP001
from logging import getLogger

from cesal_logger import setup_logging
from cesal_scraper import HousingAvailabilityChecker, check_working_hours
from cesal_scraper.constants import DEBUG

LOGGER = getLogger(__name__)


def main() -> None:
    LOGGER.info("Checking housing availability...")
    check_working_hours()
    checker = HousingAvailabilityChecker()
    checker.check_availabilities()


if __name__ == "__main__":
    setup_logging(DEBUG)
    main()
