import re
from logging import getLogger
from pathlib import Path

import requests
from cesal_logger import setup_logging
from notification import send_notification
from settings import ARRIVAL_DATE, DEBUG, DEPARTURE_DATE, EMAIL, PASSWORD

LOGGER = getLogger(__name__)


NO_HOUSING_AVAILABLE = "Aucun logement disponible"
NUMBER_OF_RESIDENCES = 6
CESAL_AUTH_COOKIES = ["CESAL_LOGEMENT", "CSLAC_LOGEMENT"]


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

    def _get_availability_payload(self, arrival_date: str, departure_date: str) -> dict[str, str]:
        """
        Get the payload to check the availability of housing in the CESAL residence.

        Args:
        ----
            arrival_date: The arrival date in the format "YYYY-MM-DD".
            departure_date (str): The departure date in the format "YYYY-MM-DD".

        Returns:
        -------
            dict[str, str]: The payload

        """
        return {"action": "modifier_date_arrivee", "date_arrivee": arrival_date, "date_sortie": departure_date}

    def check_availability(self) -> None:
        """
        Check the availability of housing in the CESAL residence.

        Raises
        ------
            Exception: If the webpage could not be retrieved.
            Exception: If the element with the id residence_{i}_logements_disponibles was not found.

        """
        payload = self._get_availability_payload(ARRIVAL_DATE, DEPARTURE_DATE)
        response = self.session.post(self.url, data=payload, timeout=10)
        html_response = response.text
        if not response.status_code == 200:
            raise Exception(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        self.dump_response(response.text, "response.html")

        pattern = r"\$\( document \)\.ready\(function\(\) \{([\s\S]*?)\}\);"

        number_of_free_housings = 0
        for i in range(1, NUMBER_OF_RESIDENCES + 1):
            pattern = rf'\$\("#residence_{i}_logements_disponibles"\)\.html\("([^"]+)"\)'
            match = re.search(pattern, html_response)

            if not match:
                raise Exception(f"Could not find the element with id residence_{i}_logements_disponibles")

            housing_status = match.group(1).strip()

            if housing_status != NO_HOUSING_AVAILABLE:
                number_of_free_housings += 1
                LOGGER.info(f"Residence {i} has housing available!")
                send_notification(residence_id=i)

        if number_of_free_housings == 0:
            LOGGER.info("No housing available.")
        else:
            LOGGER.info(f"{number_of_free_housings} housing(s) available!")

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
    setup_logging(DEBUG)
    main()
