from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    assert extract_city("123 W Main, Rexburg, ID 83440") == "Rexburg"
    assert extract_city("78 Pine St, Avon Park, FL 33825") == "Avon Park"


def test_extract_state():
    assert extract_state("123 W Main, Rexburg, ID 83440") == "ID"
    assert extract_state("78 Pine St, Avon Park, FL 33825") == "FL"


def test_extract_zipcode():
    assert extract_zipcode("123 W Main, Rexburg, ID 83440") == "83440"
    assert extract_zipcode("78 Pine St, Avon Park, FL 33825") == "33825"

pytest.main(["-v", "--tb=line", "-rN", __file__])