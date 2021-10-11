import requests
import os
import json
import logging as logger
from dotenv import load_dotenv


class RequestsUtility(object):

    def __init__(self):
        load_dotenv()
        self.base_url = os.getenv('base_url')

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f"Bad Status code." \
                                                              f"Expected {self.expected_status_code}, Actual status code: {self.status_code}," \
                                                              f"URL: {self.url}, Response Json: {self.rs_json}"

    def post(self, endpoint, payload=None, headers=None,expected_status_code=200,json_type=True):

        if not headers:
            headers = {"Content-Type": "application/json", "accept": "application/json"}

        self.url = self.base_url + endpoint
        if json_type:
            payload = json.dumps(payload)
        rs_api = requests.post(url=self.url, data=payload, headers=headers)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()
        logger.debug(f"POST API response: {self.rs_json}")
        return self.rs_json

    def get(self, endpoint, payload=None, headers=None, expected_status_code=200,**kwargs):

        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoint
        rs_api = requests.get(url=self.url, data=json.dumps(payload), headers=headers, **kwargs)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"GET API response: {self.rs_json}")

        return self.rs_json

    def patch(self, endpoint, payload=None, headers=None, expected_status_code=200, json_type=True):

        if not headers:
            headers = {"Content-Type": "application/json", "accept": "application/json"}

        self.url = self.base_url + endpoint
        if json_type:
            payload = json.dumps(payload)
        rs_api = requests.patch(url=self.url, data=payload, headers=headers)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()
        logger.debug(f"POST API response: {self.rs_json}")
        return self.rs_json


    def delete(self,endpoint,payload=None,headers=None,json_type=True,expected_status_code=200):
        self.url = self.base_url + endpoint
        if not headers:
            headers= {"Content-Type": "application/json"}
        if json_type:
            payload=json.dumps(payload)
        rs_api = requests.delete(url=self.url, data=payload, headers=headers)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        # self.rs_json = rs_api.json()
        self.assert_status_code()



if __name__ == '__main__':
    r = RequestsUtility()
    country_id = 227
    res = r.get(f"auth/countries/?search={country_id}")
    print(res)
