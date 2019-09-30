from pyourls3 import client, exceptions
import pytest
import tests
import tests.sharevar


# tests for the stats function
@pytest.fixture(scope="module")
def instance():
    c = client.Yourls(tests.sharevar.standard_url, key="12345")
    yield c
    tests.sharevar.modifier = None


def test_s_garbled_json(instance):
    tests.sharevar.modifier = "garbledjson"
    with pytest.raises(exceptions.Pyourls3HTTPError):
        instance.stats()
