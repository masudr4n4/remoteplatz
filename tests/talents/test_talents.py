from src.utilities.request_utility import RequestsUtility
import pytest

tech_ids = [46, 47, 55, 58]


def test_talent_profile(get_client_auth):
    talent_id = 2131
    r = RequestsUtility()
    res = r.get("clients/list_analytics/", headers=get_client_auth)
    dev_list = res['recommended_talents']
    # assert len(dev_list) > 0,"Recomonded talants return zero list"
    res = r.get(f"talents/{talent_id}", headers=get_client_auth)  # here have to choose talants randomly from the talents list
    print(f"User email:{res['email']},user id:{res['id']}")
    assert res['role'] == 'talent'


@pytest.mark.parametrize("tech_id", tech_ids)
def test_talant_search(get_client_auth, tech_id):
    r = RequestsUtility()
    res = r.get(f'talents/?technologies={tech_id}', headers=get_client_auth)
    assert res['previous'] == None
    assert type(res['count']) == int
    assert res['count'] > 0
    assert res.__contains__('results')
    print(f"Total talents returned {len(res['results'])}")


def test_techno_list():
    r = RequestsUtility()
    res = r.get("talents/technology/")
    print(res[0])
    assert len(res) > 0
    assert res[0].__contains__('id')
    assert res[0].__contains__('name')
    assert res[0].__contains__('type')