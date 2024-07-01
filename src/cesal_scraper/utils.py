import sys
from datetime import datetime
from logging import getLogger

from .constants import DEBUG, TIMEZONE, WORKING_HOURS

LOGGER = getLogger(__name__)


def check_working_hours() -> None:
    """
    Check if the current time is within the working hours. If so, exit the program.

    Won't exit if the DEBUG flag is set to True.
    """
    if DEBUG:
        return

    if not WORKING_HOURS[0] <= datetime.now(tz=TIMEZONE).hour < WORKING_HOURS[1]:
        LOGGER.info("Outside of working hours. Skipping...")
        sys.exit()
