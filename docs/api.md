# API reference

This is just the output of the `help` command. More comprehensive API documentation to come.

     class Yourls(builtins.object)
     |  Yourls(addr, user=None, passwd=None, key=None)
     |  
     |  Base class for Pyourls3
     |  
     |  :param addr: required, string. The base address that the YOURLS installation resides at.
     |  :param user: string. Username if not using key authorisation
     |  :param passwd: required if using user, string. Password for username/password auth.
     |  :param key: string. Can only be used if user and password are not specified.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, addr, user=None, passwd=None, key=None)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  expand(self, url)
     |      Expands a specified URL or alias into it's full form.
     |      
     |      :param url: required, string. URL or alias for shortened link.
     |      :return: string. Expanded URL.
     |  
     |  shorten(self, url, keyword=None, title=None)
     |      Sends an API request to shorten a specified URL.
     |      
     |      :param url: required, string. URL to be shortened.
     |      :param keyword: string. Custom alias for the URL
     |      :param title: string. Custom title for  the URL.
     |      :return: dictionary. Full JSON response from the API, parsed into a dict
     |      
     |      :raises: pyourls3.exceptions.Pyourls3ParamError, pyourls3.exceptions.Pyourls3HTTPError,
     |        pyourls3.exceptions.Pyourls3APIError, pyourls3.exceptions.Pyourls3URLAlreadyExistsError
     |  
     |  stats(self)
     |      Returns the overall installation stats.
     |      
     |      :return: string. Partial JSON response returned by the API.
     |      
     |      :raises: pyourls3.exceptions.Pyourls3HTTPError
     |  
     |  url_stats(self, url)
     |      Detailed stats about a specifc URL or alias.
     |      
     |      :param url: required, string. URL or alias of target redirect.
     |      :return: dict. Partial JSON response, parsed into a dict.
     |      
     |      :raises: pyourls3.exceptions.Pyourls3HTTPError, pyourls3.exceptions.Pyourls3APIError
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)