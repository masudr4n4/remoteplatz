from src.utilities.request_utility import RequestsUtility


def test_notification_cl(get_client_auth):
    r = RequestsUtility()
    res = r.get("notifications/", headers=get_client_auth)
    assert type(res['results']) == list
    assert res.__contains__('count')
    print(f"Notification found : {res['count']}")


def test_notification_dev(get_dev_auth):
    r = RequestsUtility()
    res = r.get("notifications/", headers=get_dev_auth)
    assert type(res['results']) == list
    assert res.__contains__('count')
    print(f"Notification found : {res['count']}")
