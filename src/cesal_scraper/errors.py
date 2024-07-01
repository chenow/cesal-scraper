class AuthNotSuccessfulError(Exception):
    def __init__(self) -> None:
        self.message = (
            "Couldn't retrieve the auth cookies from the CESAL website. Have you provided the correct credentials?"
        )
        super().__init__(self.message)


class ImpossibleToParseError(Exception):
    def __init__(self, residence_id: int) -> None:
        self.message = (
            f"Couldn't parse the housing availability information for residence {residence_id}. "
            "The website may have changed."
        )
        super().__init__(self.message)
