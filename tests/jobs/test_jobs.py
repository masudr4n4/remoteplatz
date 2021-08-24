from src.utilities.request_utility import RequestsUtility
from src.utilities.general import dev_auth_header
import random


def test_talents_job_list():
    """
    Get list of available job as developer
    :return:
    get jobs list
    """
    s = dev_auth_header()
    r = RequestsUtility().get("jobs/get_talent_jobs/", headers=s)
    assert len(r['results']) > 0


def test_create_job(get_client_auth):
    payload = {
        "title": f"QA Automation #{str(random.randint(1000, 2000))}",
        "salary": str(random.randint(100, 200)),
        "country_id": 271,  # Bangladesh
        "city_id": 563,
        "requirements": "Testing job description here.",
        "currency": "dollar",
        "flexibility": None,
        "job_type": "40hr/week",
        "technologies": [55],
        "timezone": "Asia/Dushanbe",
        "urgency": "ASAP",
        "client": 102
    }
    r = RequestsUtility()
    res = r.post('jobs/', payload=payload, headers=get_client_auth)
    print(f"Massage:{res['message']},title:{res['Job']['title']}")
    assert res['message'] == "Job created"

def test_apply_job(get_client_auth,get_dev_auth):
    payload = {
        "title": f"QA Automation #{str(random.randint(1000, 2000))}",
        "salary": str(random.randint(100, 200)),
        "country_id": 271,  # Bangladesh
        "city_id": 563,
        "requirements": "Testing job description here.",
        "currency": "dollar",
        "flexibility": None,
        "job_type": "40hr/week",
        "technologies": [55],
        "timezone": "Asia/Dushanbe",
        "urgency": "ASAP",
        "client": 102
    }
    r = RequestsUtility()
    res = r.post('jobs/', payload=payload, headers=get_client_auth)
    print(res)
    print(f"Massage:{res['message']},title:{res['Job']['title']}")
    assert res['message'] == "Job created"
    apply_payload = {
        "job_id": res['Job']['id']
    }
    apply_res = r.post("jobs/applications/", payload=apply_payload, headers=get_dev_auth, expected_status_code=201)
    assert res['message'] == 'Applied for job', "Applying to job failed"



# @pytest.mark.jobs
# def test_apply_to_jobs(get_client_auth):
#     print(get_client_auth)
#
# @pytest.mark.jobs
# def test_apply_to_job(get_client_auth):
#     print(get_client_auth)

def test_job_details(get_client_auth):
    job_id = 22
    r = RequestsUtility()
    res = r.get(f"jobs/{job_id}", headers=get_client_auth)
    print(f"\nid:{res['id']},title:{res['title']}")
    assert res['id'] == job_id, "Job id not matching"


def test_fixture_with_request(practice_fix):
    print("\nCalling inside the test function3")
    print(practice_fix)
    assert 0

