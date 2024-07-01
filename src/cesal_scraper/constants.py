import os

import pytz

# Auth
DEBUG = os.environ.get("DEBUG") == "1"
EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]


# User input
ARRIVAL_DATES = os.environ["ARRIVAL_DATES"].split(",")
DEPARTURE_DATE = os.environ["DEPARTURE_DATE"]
WORKING_HOURS = (8, 20)


# Cesal website constants
NO_HOUSING_AVAILABLE = "Aucun logement disponible"
NUMBER_OF_RESIDENCES = 6
CESAL_AUTH_COOKIES = ["CESAL_LOGEMENT", "CSLAC_LOGEMENT"]
CESAL_URL = "https://logement.cesal.fr/espace-resident/cesal_mon_logement_reservation.php"
CESAL_LOGIN_URL = "https://logement.cesal.fr/espace-resident/cesal_login.php"


# Timezone
TIMEZONE = pytz.timezone("Europe/Paris")
