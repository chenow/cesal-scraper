class ImpossibleToSendNotificationError(Exception):
    def __init__(self) -> None:
        self.message = (
            "Couldn't send a notification trough Telegram. "
            "Have you correctly set up the bot, or provided the right bot and chat ids?"
        )
