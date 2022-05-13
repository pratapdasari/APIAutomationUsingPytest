import requests
import json
import jsonpath
from PytestFramework.conf import urls;
from PytestFramework.data.JsonData import UserPostData

#get rid-off ssl exceptions
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


def supervisorLogin():
    #setup
    url = urls.base_url + urls.login
    jsonData = json.loads(UserPostData)

    # Get response
    response = requests.post(url, json=jsonData, verify=False)

    # Parse response to json response
    json_response = json.loads(response.text)
    return json_response

# get all property values
client_id = jsonpath.jsonpath(supervisorLogin(),'clientId')
full_name = jsonpath.jsonpath(supervisorLogin(),'fullName')
msg = jsonpath.jsonpath(supervisorLogin(),'message')
Token = jsonpath.jsonpath(supervisorLogin(),'token')




