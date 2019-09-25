class Pyourls3Error(Exception):
    # base exception
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class Pyourls3ParamError(Pyourls3Error):
    def __init__(self, param):
        self.param = param

    def __str__(self):
        return "Parameter '{}' is either missing and required, or is malformed.".format(self.param)


class Pyourls3HTTPError(Pyourls3Error):
    def __init__(self, status_code, url):
        self.status_code = status_code
        self.url = url

    def __str__(self):
        return "A HTTP error was encountered during a request to {} - {}".format(self.url, self.status_code)


class Pyourls3APIError(Pyourls3Error):
    def __init__(self, message, code):
        self.message = message
        self.code = code

    def __str__(self):
        return "An error was returned from the server during a request - {} ({})".format(self.message, self.code)


class Pyourls3URLAlreadyExistsError(Pyourls3APIError):
    def __init__(self, url):
        self.url = url

    def __str__(self):
        return "There is already a redirect to the specified URL ({}) in the database".format(self.url)
