# Welcome to Pyourls3

A Python 3 API wrapper for [[YOURLS]](https://yourls.org/) - Pyourls3 is an API wrapper module written specifically for Python 3, to work with the YOURLS link shortener. It's
designed to supersede the old [[`python-yourls`]](https://www.github.com/tflink/python-yourls) written by [[tflink]](https://github.com/tflink),
built using the fantastic [[`requests`]](https://pypi.org/project/requests/) library.

## Quick links

* [[API reference]](api.md)
* [[Getting started]](start.md)
* [[Testing and contributing]](tests.md)
* [[User guide]](manual.md)

## Project layout

    pyourls3/               # main Python package
        __init__.py
        client.py           # main file
        exceptions.py
    tests/
        __init__.py
        sharevar.py         # used to share data between tests and the Flask server
        test_expand.py      # test for the expand function
        test_init.py
        test_shorten.py
        test_stats.py
        test_url_stats.py
        webserver.py        # Flask webserver
    .gitignore
    .travis.yml
    CODE_OF_CONDUCT.md
    LICENCE
    README.md
    pytest.ini
    requirements.txt