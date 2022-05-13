import jsonpath
import requests

from PytestFramework.PytestTests.test_TC_003_fixtures import test_get_kba_categories, test_get_kba_types, \
    test_get_kba_classification, get_auth_token
from PytestFramework.conf import urls
from PytestFramework.helpers.userAuth import supervisorLogin


def getKbaId():
    #setup
    url = urls.base_url + urls.Create_Knowledge_Base
    create_kba_body = {"type": test_get_kba_types().article_id, "status": 0, "visibility": 0, "category": test_get_kba_categories().category_id,
                       "classification": test_get_kba_classification().general_classification_id, \
                       "items": [0], "kbaCustomFields": [{"id": 0, "value": "string"}], "title": "KBA from pytest",
                       "summary": "KBA from pytest", "body": "KBA from pytest"}
    Token = jsonpath.jsonpath(supervisorLogin(), 'token')
    auth = {"Authorization": "Bearer {}".format(Token[0])}

    # Process
    response = requests.post(url, json=create_kba_body, headers=auth, verify=False)

    # Verification
    response_body = response.json()
    print(response_body)
    assert response.status_code == 200
    return response_body