# noqa: INP001
from logging import getLogger

from cesal_scraper import HousingAvailabilityChecker, setup_logging
from cesal_scraper.settings import DEBUG

LOGGER = getLogger(__name__)


def main() -> None:
    url = "https://logement.cesal.fr/espace-resident/cesal_mon_logement_reservation.php"
    login_url = "https://logement.cesal.fr/espace-resident/cesal_login.php"
    LOGGER.info("Checking housing availability...")
    checker = HousingAvailabilityChecker(url, login_url)
    checker.check_availability()


if __name__ == "__main__":
    setup_logging(DEBUG)
    main()
