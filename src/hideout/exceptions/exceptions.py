class HideoutException(Exception):
    """The base exceptrion object."""
    pass


class InvalidAccessToken(HideoutException):
    """The exception that gets thrown when an invalid access token is present."""

    def __init__(self):
        message = "An invalid access token is present."
        super(InvalidAccessToken, self).__init__(message)


class ConnectionTaken(HideoutException):
    """The exception that gets thrown when another client has already taken the connection."""

    def __init__(self):
        message = "Another client has already taken the connection."
        super(ConnectionTaken, self).__init__(message)


class NoConnectionException(HideoutException):
    """The exception that gets thrown when an action gets executed while no connection has been established yet."""

    def __init__(self):
        message = "No connection has been established yet."
        super(NoConnectionException, self).__init__(message)