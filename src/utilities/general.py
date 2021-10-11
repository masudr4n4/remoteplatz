import random
import string
import logging as logger
from py.path import local
import os
from src.data.static_data import data
import requests
from dotenv import load_dotenv

def get_random_email():
    """
    Generating an email with fixed prefix and suffix.
    then returning the email
    """
    email_prefix = 'akib_'
    string_ = "".join(random.choice(string.ascii_lowercase) for i in range(6))
    email = email_prefix + string_ + '@rmtplatz.com'
    logger.info(f"Generated Email address: {email}")
    return email

def get_random_string(lenght=5):
    return "".join(random.choice(string.ascii_lowercase) for i in range(lenght))

def generate_phon_number(country_code="880"):
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    string_ = "".join(str(random.choice(num)) for i in range(11 - len(country_code)))
    return string_


def gen_f_name():
    return "Akib"


def gen_l_name():
    return "test"


def get_cv_sample():
    project_path = local(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    file = project_path + '/data/sample.pdf'
    return open(file, 'rb')


def dev_auth_header():
    load_dotenv()
    os.getenv('base_url')
    mail = data['dev_user']['email']
    payload = {
        "email": mail,
        "password": data['dev_user']['password']
    }
    res = requests.post(os.getenv('base_url')+"auth/token/", data=payload)
    res.headers.update({"authorization": "Bearer "+res.json()['token']})
    return res.headers

def client_auth_header():
    load_dotenv()
    os.getenv('base_url')
    mail = data['client_user']['email']
    payload = {
        "email": mail,
        "password": data['client_user']['password']
    }
    res = requests.post(os.getenv('base_url')+"auth/token/", data=payload)
    res.headers.update({"authorization": "Bearer "+res.json()['token']})
    return res.headers


def get_random_location():
    countries = requests.get('auth/countries/')
    countries_id = []
    for country in countries:
        countries_id.append(country['id'])
    random_country_id = random.choice(countries_id)
    cities = requests.get(f"auth/cities/?country={random_country_id}")
    return cities


def get_random_string():
    st =  "".join(random.choice(string.ascii_lowercase) for i in range(6))
    print(st)
    return st

if __name__ == "__main__":
    dev_auth_header()
