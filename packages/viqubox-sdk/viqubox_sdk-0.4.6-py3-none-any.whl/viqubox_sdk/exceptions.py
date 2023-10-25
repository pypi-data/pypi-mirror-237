class APIRequestError(Exception):
    """Exception raised whenever the API returns a bad response code.

    :param Exception: Custom exception message related to the API error.
    """


class AuthException(Exception):
    """Exception raised whenever there are issues with API authentication.

    This includes a missing username or password if only one of them is provided.
    """
