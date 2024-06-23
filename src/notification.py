from logging import getLogger

import requests
from settings import BOT_TOKEN, CHAT_ID

LOGGER = getLogger(__name__)


def send_notification(residence_id: int) -> None:
    """
    Send a telegram notification to the user to say that a housing is available.

    Args:
    ----
        residence_id: The ID of the residence where the housing is available.

    """
    message = f"Logement disponible à la résidence {residence_id} !"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
    response = requests.get(url, timeout=5)
    LOGGER.info(f"{response.status_code}: {response.json()}")
