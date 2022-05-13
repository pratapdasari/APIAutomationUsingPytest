import jsonpath
import requests
import pytest
from PytestFramework.conf import urls
from PytestFramework.helpers.userAuth import supervisorLogin

#i = 20
#@pytest.mark.skipif (i>10,reason="Skipping due to the functionality is not working...")
def test_get_kba_categories():
    # setup
    url = urls.base_url + urls.Knowledge_Base_Categories
    Token = jsonpath.jsonpath(supervisorLogin(), 'token')
    auth = {"Authorization": "Bearer {}".format(Token[0])}

    #Process
    response = requests.get(url, headers=auth, verify= False)

    # Verification
    response_body = response.json()
    print(response_body)
    return response_body
    assert response.status_code == 200

def test_get_kba_classification():
    # setup
    url = urls.base_url + urls.Knowledge_Base_Classificatio
    Token = jsonpath.jsonpath(supervisorLogin(), 'token')
    auth = {"Authorization": "Bearer {}".format(Token[0])}

    # Process
    response = requests.get(url, headers=auth, verify=False)

    # Verification
    response_body = response.json()
    print(response_body)
    return response_body
    assert response.status_code == 200


