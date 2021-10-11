from src.utilities.request_utility import RequestsUtility
from src.utilities.general import get_random_string

def test_update_profile(get_dev_auth):
    data = {
        'id': 2131,
        'country_id': 271,
        'bio': f'Tester Qa automation api {get_random_string()}',
        'first_name': 'Tohfa',
        "last_name" : " Akib",
        "city_id": 616,
        # "dob": "2001 - 07 - 05",
        # "phone_code": "+880",
        # "phone": "1701007651"
    }
    r = RequestsUtility()
    res = r.patch('talents/update_my_profile/', payload=data, headers=get_dev_auth, json_type=True)
    print(res)
    assert res['message'] == "Updated talent profile successfully",f"Actual message was {res['message']}"
    print(res['message'])
