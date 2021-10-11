from src.utilities.request_utility import RequestsUtility
from src.utilities.general import dev_auth_header
import random
from datetime import datetime, timedelta


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
    """
    IF this test case fail then make sure the client id is correct.
    """
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
        "client": 2150
    }
    r = RequestsUtility()
    res = r.post('jobs/', payload=payload, headers=get_client_auth)
    print(f"Massage:{res['message']},job id: {res['Job']['id']} ,title:{res['Job']['title']}")
    assert res['message'] == "Job created"


def test_pause_active_delete_job(get_client_auth):
    """
    IF this test case fail check the client id number
    """
    data = {
        "title": f"QA Automation #{str(random.randint(1000, 2000))}",
        "salary": str(random.randint(100, 200)),
        "country_id": 271,  # Bangladesh
        "city_id": 563,
        "requirements": "Testing automated job description here.",
        "currency": "dollar",
        "flexibility": None,
        "job_type": "40hr/week",
        "technologies": [55],
        "timezone": "Asia/Dushanbe",
        "urgency": "ASAP",
        "client": 2150
    }
    r = RequestsUtility()
    res = r.post('jobs/', payload=data, headers=get_client_auth, json_type=True)
    job_id = res['Job']['id']
    pause = {'status':'paused'}
    active = {'status':'active'}
    res = r.patch(f"jobs/{job_id}/", payload=pause, headers=get_client_auth, json_type=True)
    assert res['job']['id'] == job_id,"Job id does not match with created one."
    assert res['job']['status'] == 'paused'
    assert res['message'] == 'Updated job'
    print(f"job id: {res['job']['id']}, Title: {res['job']['title']},Job Status now: {res['job']['status']}")
    res = r.patch(f"jobs/{job_id}/", payload=active, headers=get_client_auth, json_type=True)
    assert res['job']['id'] == job_id,"Job id does not match with created one."
    assert res['job']['status'] == 'active'
    assert res['message'] == 'Updated job'
    print(f"job id: {res['job']['id']}, Title: {res['job']['title']},Job Status now: {res['job']['status']}")
    r.delete(f"jobs/{job_id}/", headers=get_client_auth, json_type=False, expected_status_code=204)
    print('Deleted the post succesfully')


def test_apply_job(get_client_auth, get_dev_auth):
    """
        IF this test case fail then make sure the client id is correct.
    """
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
        "client": 2150
    }
    r = RequestsUtility()
    res = r.post('jobs/', payload=payload, headers=get_client_auth)
    # print(res)
    print(f"Massage:{res['message']},title:{res['Job']['title']}")
    assert res['message'] == "Job created"
    apply_payload = {
        "job_id": res['Job']['id']
    }
    apply_res = r.post("jobs/applications/", payload=apply_payload, headers=get_dev_auth, expected_status_code=201)
    assert apply_res['message'] == 'Applied for job', "Applying to job failed"


def test_job_details(get_client_auth):
    job_id = 230
    r = RequestsUtility()
    res = r.get(f"jobs/{job_id}", headers=get_client_auth)
    print(f"\nid:{res['id']},title:{res['title']}")
    # print(res)
    assert res['id'] == job_id, "Job id not matching"


def test_job_list_client_posted(get_client_auth):
    r = RequestsUtility()
    res = r.get("jobs/get_client_jobs/", headers=get_client_auth)
    print(f"\nClient posted {len(res['results'])} jobs")
    assert type(res['results']) == list


def test_invite_dev_for_job(get_client_auth):
    """
    get job list for client user get the id for job.
    invite someone from recomonded dev
    :param get_client_auth:
    :return:
    """
    r = RequestsUtility()
    job_res = r.get("jobs/get_client_jobs/", headers=get_client_auth)
    job_ids=[job['id'] for job in job_res['results']]
    print(f"job id's list :{job_ids}")
    res = r.get("talents/",headers=get_client_auth)
    talent_ids = [profile['id'] for profile in res['results']]
    print(f"Talents id's list: {talent_ids}")
    payload = {"talent_id": random.choice(talent_ids), "job_id": random.choice(job_ids),
               "client_slots": [str(datetime.now().isoformat()), str((datetime.now()+timedelta(days=1)).isoformat())]}
    print(payload)
    res = r.post("invitations/", payload= payload, headers=get_client_auth, expected_status_code=201)
    assert res['message'] == 'created Invitation successfully!',"Can not invite talents to a job"