import requests
import urllib3
from pyourls3 import exceptions, version
import json


class Yourls:
    """
    Base class for Pyourls3

    :param addr: required, string. The base address that the YOURLS installation resides at.
    :param user: string. Username if not using key authorisation
    :param passwd: required if using user, string. Password for username/password auth.
    :param key: string. Can only be used if user and password are not specified.
    """

    def __init__(self, addr, user=None, passwd=None, key=None):

        if not addr:
            raise exceptions.Pyourls3ParamError("API URL")

        scheme, _, _, _, _, _, _ = urllib3.util.parse_url(addr)  # checking for a protocol in the URL

        if not scheme:
            raise exceptions.Pyourls3ParamError("addr")

        self.using_signature_auth = False

        if user is None or passwd is None:
            if key is None:
                raise exceptions.Pyourls3ParamError("username and password or signature")
            else:
                if type(key) is not str:
                    raise exceptions.Pyourls3ParamError("key")
                self.using_signature_auth = True
                self.global_args = {"signature": key}
        else:
            if type(user) is not str:
                raise exceptions.Pyourls3ParamError("user")
            elif type(passwd) is not str:
                raise exceptions.Pyourls3ParamError("passwd")
            self.global_args = {"username": user, "password": passwd}

        self.global_args["format"] = "json"

        if addr[-1] != "/":  # I like trailing slashes
            addr += "/"

        self.api_endpoint = addr + "yourls-api.php"

        self.session = requests.session()
        self.session.headers.update = {"user-agent": "pyourls3/{}".format(version)}

    def shorten(self, url, keyword=None, title=None):
        """
        Sends an API request to shorten a specified URL.

        :param url: required, string. URL to be shortened.
        :param keyword: string. Custom alias for the URL
        :param title: string. Custom title for  the URL.
        :return: dictionary. Full JSON response from the API, parsed into a dict

        :raises: pyourls3.exceptions.Pyourls3ParamError, pyourls3.exceptions.Pyourls3HTTPError,
          pyourls3.exceptions.Pyourls3APIError, pyourls3.exceptions.Pyourls3URLAlreadyExistsError
        """

        if not url:
            raise exceptions.Pyourls3ParamError("url")

        specific_args = {"action": "shorturl", "url": url}

        if keyword is not None:
            specific_args["keyword"] = keyword

        if title is not None:
            specific_args["title"] = title

        r = requests.post(self.api_endpoint, data={**self.global_args, **specific_args})
        try:
            j = r.json()
        except json.decoder.JSONDecodeError:
            raise exceptions.Pyourls3HTTPError(r.status_code, self.api_endpoint)

        if not j["status"] == "success":
            if j["code"] == "error:url":
                raise exceptions.Pyourls3URLAlreadyExistsError(url)
            else:
                raise exceptions.Pyourls3APIError(j["message"], j["code"])

        return j

    def expand(self, url):
        """
        Expands a specified URL or alias into it's full form.

        :param url: required, string. URL or alias for shortened link.
        :return: string. Expanded URL.
        """

        if not url:
            raise exceptions.Pyourls3ParamError("url")

        specific_args = {"action": "expand", "shorturl": url}

        r = requests.post(self.api_endpoint, data={**self.global_args, **specific_args})
        try:
            j = r.json()
        except json.decoder.JSONDecodeError:
            raise exceptions.Pyourls3HTTPError(r.status_code, self.api_endpoint)

        if not j["message"] == "success":
            raise exceptions.Pyourls3APIError(j["message"].split(": ")[1], j["code"])  # message returns "error: blah"

        return j["longurl"]

    def stats(self):
        """
        Returns the overall installation stats.

        :return: string. Partial JSON response returned by the API.

        :raises: pyourls3.exceptions.Pyourls3HTTPError
        """

        specific_args = {"action": "stats"}

        r = requests.post(self.api_endpoint, data={**self.global_args, **specific_args})
        try:
            j = r.json()
        except json.decoder.JSONDecodeError:
            raise exceptions.Pyourls3HTTPError(r.status_code, self.api_endpoint)

        return j["stats"]

    def url_stats(self, url):
        """
        Detailed stats about a specifc URL or alias.

        :param url: required, string. URL or alias of target redirect.
        :return: dict. Partial JSON response, parsed into a dict.

        :raises: pyourls3.exceptions.Pyourls3HTTPError, pyourls3.exceptions.Pyourls3APIError
        """

        if not url:
            raise exceptions.Pyourls3ParamError("url")

        specific_args = {"action": "url-stats", "shorturl": url}

        r = requests.post(self.api_endpoint, data={**self.global_args, **specific_args})
        try:
            j = r.json()
        except json.decoder.JSONDecodeError:
            raise exceptions.Pyourls3HTTPError(r.status_code, self.api_endpoint)

        if not j["message"] == "success":
            raise exceptions.Pyourls3APIError(j["message"].split(": ")[1], j["code"])  # message returns "error: blah"

        return j["link"]