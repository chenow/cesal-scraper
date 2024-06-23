from logging import getLogger
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from cesal_logger import setup_logging
from settings import DEBUG, EMAIL, PASSWORD

setup_logging(DEBUG)

LOGGER = getLogger(__name__)


NO_HOUSING_AVAILABLE = "Aucun logement disponible"
NUMBER_OF_RESIDENCES = 6
CESAL_AUTH_COOKIES = [
    "CESAL_LOGEMENT",
    #   "CSLAC_LOGEMENT"
]


class HousingAvailabilityChecker:
    """Used to check the availability of housing in the CESAL residence."""

    def __init__(self, url: str, login_url: str) -> None:
        """
        Initialize the HousingAvailabilityChecker object.

        Args:
        ----
            url: The URl of CESAL containing the housing availability information.
            login_url: The URL of the login page.

        """
        self.url = url
        self.login_url = login_url
        self.session = requests.Session()
        self._authenticate()

    def _authenticate(self) -> None:
        """Login to the CESAL website to get auth COOKIES."""
        payload: dict[str, str] = {
            "action": "login",
            "login-email": EMAIL,
            "login-password": PASSWORD,
            "login-remember-me": "on",
        }
        response = self.session.post(self.login_url, data=payload)

        if response.status_code != 200:
            raise Exception(f"Failed to login. Status code: {response.status_code}")

        if any(cookie not in self.session.cookies for cookie in CESAL_AUTH_COOKIES):
            raise Exception("CESAL_AUTH_COOKIES not found in login response.")

        LOGGER.debug(f"Cookies: {self.session.cookies}")
        LOGGER.info("Authentication successful")

    def check_availability(self) -> None:
        """
        Check the availability of housing in the CESAL residence.

        Raises
        ------
            Exception: If the webpage could not be retrieved.
            Exception: If the element with the id residence_{i}_logements_disponibles was not found.

        """
        payload = {
            "action": "modifier_date_arrivee",
            "date_arrivee": "2024-07-12",
            "avec_heure_arrivee_2024-06-28": "0",
            "avec_heure_arrivee_2024-07-01": "0",
            "avec_heure_arrivee_2024-07-02": "0",
            "avec_heure_arrivee_2024-07-03": "0",
            "avec_heure_arrivee_2024-07-04": "0",
            "avec_heure_arrivee_2024-07-05": "0",
            "avec_heure_arrivee_2024-07-08": "0",
            "avec_heure_arrivee_2024-07-09": "0",
            "avec_heure_arrivee_2024-07-10": "0",
            "avec_heure_arrivee_2024-07-11": "0",
            "avec_heure_arrivee_2024-07-12": "0",
            "avec_heure_arrivee_2024-07-15": "0",
            "avec_heure_arrivee_2024-07-16": "0",
            "avec_heure_arrivee_2024-07-17": "0",
            "date_sortie": "30/04/2025",
        }
        response = self.session.post(self.url, data=payload, timeout=10)
        if not response.status_code == 200:
            raise Exception(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        soup = BeautifulSoup(response.content, "html.parser")
        self.dump_response(response.text, "response.html")

        for i in range(1, NUMBER_OF_RESIDENCES + 1):
            residence_id = f"residence_{i}_logements_disponibles"
            element = soup.find(id=residence_id)
            if not element:
                raise Exception(f"Element with id {residence_id} not found")

            text = element.get_text(strip=True)
            if text == NO_HOUSING_AVAILABLE:
                LOGGER.info(f"Residence {i}: No housing available")

            LOGGER.info(f"Residence {i}: Housing available")

    def dump_response(self, response: str, filename: str) -> None:
        """
        Dump the response to a file for debugging purposes.

        Args:
        ----
            response: The response to dump.
            filename: The name of the file to dump the response to.

        """
        if not DEBUG:
            return

        path = Path(f"temp/{filename}")
        with path.open("w") as file:
            file.write(response)


def main() -> None:
    url = "https://logement.cesal.fr/espace-resident/cesal_mon_logement_reservation.php"
    login_url = "https://logement.cesal.fr/espace-resident/cesal_login.php"
    LOGGER.info("Checking housing availability...")
    checker = HousingAvailabilityChecker(url, login_url)
    checker.check_availability()


if __name__ == "__main__":
    main()
