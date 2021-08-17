from src.utilities.request_utility import RequestsUtility
import pytest

coutries_id = (255, 267, 258,314, 263, 271)


def test_country_list():
    r = RequestsUtility()
    res = r.get('auth/countries/')
    print(res)
    assert type(res) == list, f"Response is not returning country list."
    assert len(res) == 252, f"Expected country list 252,we got {len(res)}"


@pytest.mark.parametrize("country_id", coutries_id)
def test_country_details(country_id):
    """
    :return: all the cities details related to the country id
    """
    print(f"Country id = {country_id}")
    r = RequestsUtility()
    res = r.get(f"auth/cities/?country={country_id}")
    print(res)
    assert len(res) > 0, f"Country cities retrieving have problems"