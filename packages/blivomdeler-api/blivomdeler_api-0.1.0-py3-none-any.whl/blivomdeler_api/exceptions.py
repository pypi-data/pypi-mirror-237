# User errors
class InvalidCredentialsError(Exception):
    pass


class LoginRequiredError(Exception):
    pass


# Other
class InternalException(Exception):
    pass
