from src.utilities.general import get_cv_sample, gen_f_name, gen_l_name, generate_phon_number, get_random_email
import requests


def test_signup_as_dev():
    payload = {
        "first_name": gen_f_name(),
        "last_name": gen_l_name(),
        "email": get_random_email(),
        "phone": generate_phon_number(),
        "password": "Demo1234",
        "phone_code": "880",
        "role": "talent",
        "cv": get_cv_sample()
    }
    print(f'Used informatoin for signing up as dev: {payload}')
    res = requests.post("https://api.remoteplatz.ch/auth/signup/", data=payload)
    # print(res.content)
    assert res.status_code == 200, f"Expected status code 200 Sign up,Received {res.status_code}"
    assert type(res.json()['user']['id']) == int, f"Id not found in the response"