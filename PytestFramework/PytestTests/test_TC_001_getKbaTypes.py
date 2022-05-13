import json
import jsonpath
import requests
import urllib3
from PytestFramework.conf import urls
from PytestFramework.helpers.userAuth import supervisorLogin
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings()
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# setup
url = urls.base_url + urls.Knowledge_Base_Types
Token = jsonpath.jsonpath(supervisorLogin(),'token')
auth = {"Authorization": "Bearer {}".format(Token[0])}


def test_get_kba_types():
    # Process
    response = requests.get(url, headers=auth, verify= False)
    # Verification
    response_body = response.json()
    print(response_body)
    assert response.status_code == 200
    assert response_body[0]["id"] == 1000
    assert response_body[0]["value"] == 'Article'
    assert response_body[3]["id"] == 4000
    assert response_body[3]["value"] == 'Solution'
