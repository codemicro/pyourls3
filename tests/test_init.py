from pyourls3 import client, exceptions
import pytest


# initialisation tests
def test_i_url_exists():
    with pytest.raises(exceptions.Pyourls3ParamError):
        client.Yourls("")


def test_i_url_schema():
    with pytest.raises(exceptions.Pyourls3ParamError):
        client.Yourls("example.com")


def test_i_url_formatting():
    url = "https://example.com"
    c = client.Yourls(url, key="12345")
    assert c.api_endpoint != url + "yourls-api.php"
    assert c.api_endpoint == url + "/yourls-api.php"


def test_i_credentials_present():
    with pytest.raises(exceptions.Pyourls3ParamError):
        client.Yourls("http://example.com")


def test_i_credential_format():
    with pytest.raises(exceptions.Pyourls3ParamError):
        client.Yourls("http://example.com", key=123456789)
    with pytest.raises(exceptions.Pyourls3ParamError):
        client.Yourls("http://example.com", user="hello", passwd=12345)
    with pytest.raises(exceptions.Pyourls3ParamError):
        client.Yourls("http://example.com", user=12345)


def test_i_user_passwd():
    client.Yourls("http://example.com", user="username", passwd="password")


def test_i_api_key():
    client.Yourls("http://example.com", key="123456789")


def test_i_user_agent():
    inst = client.Yourls("http://example.com", key="1234")
    assert "user-agent" in inst.session.headers.update


