from src.utilities.request_utility import RequestsUtility


def test_talent_profile(get_client_auth):
    r = RequestsUtility()
    res = r.get("clients/list_analytics/", headers=get_client_auth)
    dev_list = res['recommended_talents']
    print(dev_list)
    # assert len(dev_list) > 0,"Recomonded talants return zero list"
    res = r.get(f"talents/112", headers=get_client_auth)  # here have to choose talants randomly from the talents list
    print(res)
    assert res['role'] == 'talent'
