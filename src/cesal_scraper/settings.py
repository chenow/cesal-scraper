import os

import pytz

# Auth
DEBUG = os.environ.get("DEBUG") == "1"
EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]
BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]


ARRIVAL_DATES = os.environ["ARRIVAL_DATES"].split(",")
DEPARTURE_DATE = os.environ["DEPARTURE_DATE"]
WORKING_HOURS = (8, 20)

TIMEZONE = pytz.timezone("Europe/Paris")
