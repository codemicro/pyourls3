
class Pyourls3Error(Exception):
    """Base exception for Pyourls3.

    :param msg: string, full exception text.
    """

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class Pyourls3ParamError(Pyourls3Error):
    """Raised when a function parameter is incorrect

    :param param: string, parameter name that caused the issue
    """

    def __init__(self, param):
        self.param = param

    def __str__(self):
        return "Parameter '{}' is either missing and required, or is malformed.".format(self.param)


class Pyourls3HTTPError(Pyourls3Error):
    """Raised in the event that a HTTP error is caused

    :param status_code: string, HTTP status code
    :param url: string, URL that generated the HTTP error
    """

    def __init__(self, status_code, url):
        self.status_code = status_code
        self.url = url

    def __str__(self):
        return "A HTTP error was encountered during a request to {} - {}".format(self.url, self.status_code)


class Pyourls3APIError(Pyourls3Error):
    """Raised when the API raises an error and returns it through JSON

    :param message: string, message sent back by API
    :param code: string, status code sent back by the API
    """

    def __init__(self, message, code):
        self.message = message
        self.code = code

    def __str__(self):
        return "An error was returned from the server during a request - {} ({})".format(self.message, self.code)


class Pyourls3URLAlreadyExistsError(Pyourls3APIError):
    """Raised specifically when the API returns an error stating the URL already has a redirect created for it
    It's derived from an API error.

    :param url: URL that's already redirected to
    """

    def __init__(self, url):
        self.url = url

    def __str__(self):
        return "There is already a redirect to the specified URL ({}) in the database".format(self.url)
