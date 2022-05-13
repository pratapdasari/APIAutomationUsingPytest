import json
import jsonpath
import requests
import pytest
from PytestFramework.conf import urls
from PytestFramework.helpers.userAuth import supervisorLogin


@pytest.fixture(scope='module')
def get_auth_token():
    global auth
    Token = jsonpath.jsonpath(supervisorLogin(), 'token')
    auth = {"Authorization": "Bearer {}".format(Token[0])}


def test_get_kba_types(get_auth_token):
    global article_id
    #setup
    url = urls.base_url + urls.Knowledge_Base_Types

    # process
    response = requests.get(url, headers=auth, verify= False)

    # Validation
    response_body = response.json()
    print(response_body)
    article_id = response_body[0]["id"]
    assert response.status_code == 200

@pytest.mark.Smoke
def test_get_kba_categories(get_auth_token):
    global category_id

    # setup
    url = urls.base_url + urls.Knowledge_Base_Categories

    #Process
    response = requests.get(url, headers=auth, verify= False)

    # Validation
    response_body = response.json()
    print(response_body)
    category_id = response_body['results'][0]["categoryId"]
    assert response.status_code == 200

@pytest.mark.Smoke
def test_get_kba_classification(get_auth_token):
    global general_classification_id
    # setup
    url = urls.base_url + urls.Knowledge_Base_Classification

    # Process
    response = requests.get(url, headers=auth, verify=False)

    # Validation
    response_body = response.json()
    print(response_body)
    general_classification_id = response_body[2]["problemTypeId"]
    assert response.status_code == 200

@pytest.mark.skip("Not Applicable")
def test_post_create_kba(get_auth_token):
    global kba_id
    # setup
    url = urls.base_url + urls.Create_Knowledge_Base
    create_kba_body = {"type": article_id,"status":0,"visibility": 0, "category": category_id,"classification": general_classification_id,\
     "items": [0],"kbaCustomFields": [{"id": 0,"value": "string"}],"title": "KBA from pytest","summary": "KBA from pytest", "body": "KBA from pytest"}

    # Process
    response = requests.post(url, json=create_kba_body, headers=auth, verify=False)

    # Validation
    response_body = response.json()
    kba_id = response_body
    print("KBA Id is :", kba_id)
    assert response.status_code == 200

@pytest.mark.skip("Not Applicable")
def test_post_add_comment_in_kba(get_auth_token):
    #setup
    url = urls.base_url + urls.Create_Knowledge_Base +"/"+str(kba_id)+"/comments"
    print(url)
    add_comment_body = {"commentText": "This comment from Pytest"}

    # Process
    response = requests.post(url, json=add_comment_body, headers=auth, verify=False)

    # Validation
    response_body = response.json()
    print(response_body)
    assert response.status_code == 200





