from src.utilities.request_utility import RequestsUtility
from src.utilities.general import dev_auth_header


def test_talents_list():
    """
    :return:
    get talents list
    """
    s = dev_auth_header()
    r = RequestsUtility().get("jobs/get_talent_jobs/", headers=s)
    assert len(r['results']) > 0
