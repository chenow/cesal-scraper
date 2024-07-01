from logging import getLogger

import requests
from cesal_scraper.constants import CESAL_URL, DEPARTURE_DATE

from .constants import BOT_TOKEN, CHAT_ID

LOGGER = getLogger(__name__)


def send_notification(residence_id: int, arrival_date: str) -> None:
    """
    Send a message to the user using a Telegram bot, if a housing is available.

    Args:
    ----
        residence_id: The ID of the residence where the housing is available.
        arrival_date: The date of arrival in the housing.

    """
    message = (
        f"Logement disponible à la résidence {residence_id} !\n\n"
        f"Date d'arrivée: {arrival_date}\n"
        f"Date de départ: {DEPARTURE_DATE}\n"
        f"Url: {CESAL_URL}"
    )

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
    response = requests.get(url, timeout=5)
    LOGGER.info(f"{response.status_code}: {response.json()}")
