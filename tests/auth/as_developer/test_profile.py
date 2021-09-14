from src.utilities.request_utility import RequestsUtility
from src.utilities.general import get_random_string

def test_update_profile(get_dev_auth):
    r = RequestsUtility()
    first_name = f"Tohfa {get_random_string()}"
    last_name = f"Akib {get_random_string()}"
    data = {
        'id': "59",
        'country_id': '271',
        'bio': 'bio',
        'first_name': first_name,
        'last_name': last_name,
        # 'city_id': '616',
        # 'dob': '2001 - 07 - 05',
        # 'phone_code': '1',
        # 'phone': '1701007651',
    }
    res = r.patch('talents/update_my_profile/', payload=data, headers=get_dev_auth, json=False)
    assert res['message'] == 'Updated talent profile successfully'
    user = res['talent']
    msg = f"User email: {user['email']},Updated first name: {user['first_name']},updated last name: {user['last_name']}"
    print(msg)
