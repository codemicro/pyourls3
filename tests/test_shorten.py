from pyourls3 import client, exceptions
import pytest
import tests
import tests.sharevar


standard_url = "http://127.0.0.1:5000/"

# tests for  the shorten function, utilises a Flask WSGI server. Data is passed from that server through sharevar.py
# it is crucial that if the modifier is used, it is RESET TO NONE when the test is complete. This can be done by using
# the fixture "instance"


@pytest.fixture(scope="module")
def instance():
    c = client.Yourls(standard_url, key="12345")
    yield c
    tests.sharevar.modifier = None


def test_s_url_exists(instance):
    with pytest.raises(exceptions.Pyourls3ParamError):
        instance.shorten("")


def test_s_keyword(instance):
    kwd = "keyword goes here"
    instance.shorten("https://www.google.com", keyword=kwd)
    assert "keyword" in tests.sharevar.last_request
    assert tests.sharevar.last_request["keyword"] == kwd


def test_s_title(instance):
    title = "this should be a title"
    instance.shorten("https://www.google.com", title=title)
    assert "title" in tests.sharevar.last_request
    assert tests.sharevar.last_request["title"] == title


def test_s_garbled_json(instance):
    tests.sharevar.modifier = "garbledjson"
    with pytest.raises(exceptions.Pyourls3HTTPError):
        instance.shorten("https://www.google.com")


def test_s_url_error(instance):
    tests.sharevar.modifier = "urlerror"
    with pytest.raises(exceptions.Pyourls3URLAlreadyExistsError):
        instance.shorten("https://www.google.com")


def test_s_other_error(instance):
    tests.sharevar.modifier = "othererror"
    with pytest.raises(exceptions.Pyourls3APIError):
        instance.shorten("https://www.google.com")
