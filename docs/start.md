# Getting started

Pyourls3 is designed to be simple. And it is! It's not unnecessarily complicated, and ease of use is focused on.

## **Installation**

The best and easiest way of installing Pyourls3 is by using `pip`.
    
    pip install pyourls3

## **Basic usage**

Pyourls3 supports both YOURLS' key authentication (see [[Passwordless API requests]](https://github.com/YOURLS/YOURLS/wiki/PasswordlessAPI)) and traditional username/password authentication. 

    import pyourls3
    
    yourls = pyourls3.Yourls("https://www.example.com", user="username", passwd="password")
    
If you're using a key instead of a username and password use
    
    yourls = pyourls3.Yourls("https://www.example.com", key="keyhere")
    
## **Your first link**

Simply running the following is enough to create a shortened link.

    response = yourls.shorten("https://www.example.com/thing/words/herro")
    
This function will either raise an exception if something was wrong, or will return a response in the form of a dictionary.
This is exactly what's returned from the API, with the exception being that this is converted into native Python datatypes
instead of raw JSON. The shortened link is contained within the `shorturl` section of the response as a string.

    >>> response["shorturl"]
    'http://www.example.com/9'
    
You can also specify a custom alias for your link, as well as a redirect title.
    
    response = yourls.shorten("https://www.example.com/thing/words/herro", key="teaisgood", title="This was long but now it's short!")
    
YOURLS' unique URLs

A config setting within YOURLS allows you to enable or disable the ability to create multiple shortened URLs for the same
long URL. If this is disabled, and a request to create a new entry for a pre-existing link is made, an exception will be 
thrown.

    >>> yourls.shorten("https://www.example.com/thing/words/herro")
    Traceback (most recent call last):
      File "<pyshell#12>", line 1, in <module>
        yourls.shorten("https://www.example.com/thing/words/herro")
      File "C:\Python37\lib\site-packages\pyourls3\client.py", line 88, in shorten
        raise exceptions.Pyourls3URLAlreadyExistsError(url)
    pyourls3.exceptions.Pyourls3URLAlreadyExistsError: There is already a redirect to the specified URL (https://www.example.com/thing/words/herro) in the database

*In a future update, instead of throwing an error, Pyourls3 will simply return the shortened URL.* 
    
## **Expanding a link**

Sometimes the situation arises when you need to expand a link that's been shortened, which is equally easy to do as shortening
in the first place, if not easier. Simply pass the full shortened URL or the alias to the `expand` function, and the original
long URL is returned in a string.

    >>> pyourls3.expand("teaisgood")
    'https://www.example.com/thing/words/herro'
    
## **Further reading**
[[API reference]](api.md)