import pytest
from src.utilities.general import client_auth_header,dev_auth_header


@pytest.fixture(scope='module')
def get_client_auth():
    """
    Setting scope as module means it will run only one time for a single test file.
    :return:
    """
    print("Just called the fixture get_client_auth function")
    return client_auth_header()


@pytest.fixture(scope='module')
def get_dev_auth():
    print("Calling for dev auth header")
    return dev_auth_header()




# @pytest.fixture(scope='function')
# def practice_fix(request):
#     print("\nCalling fixture1")
#     print(dir(request),2)
#     print(request.node.name)
#     print(request.node.nodeid)
#     print('test status',request.session.testsfailed)
#     yield "\nYield return from fixture4"
#     print(request.session.testsfailed)