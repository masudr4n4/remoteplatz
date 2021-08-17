import requests
from src.utilities.general import get_random_email, generate_phon_number, gen_f_name, gen_l_name


def test_client_signup():

    payload = {
        "first_name": gen_f_name(),
        "last_name": gen_l_name(),
        "email": get_random_email(),
        "phone": generate_phon_number(),
        "name": "Appics AG",
        "password": "Demo1234",
        "phone_code": "880",
        "role": "client"
    }
    print(f'Used informatoin for signing up {payload}')
    res = requests.post("https://api.remoteplatz.ch/auth/signup/", data=payload)
    assert res.status_code == 200, f"Expected status code 200 ,Received {res.status_code}"
    assert type(res.json()['id']) == int,f"Id not found in the response"
