class AuthNotSuccessfulError(Exception):
    def __init__(self) -> None:
        self.message = (
            "Couldn't retrieve the auth cookies from the CESAL website. Have you provided the correct credentials?"
        )
        super().__init__(self.message)
