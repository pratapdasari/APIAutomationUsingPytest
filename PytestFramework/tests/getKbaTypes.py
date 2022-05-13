#API Url
import requests
import json
import jsonpath

from PytestFramework.conf import urls;
from PytestFramework.tests.UserAuth import userLogin

Token = jsonpath.jsonpath(userLogin(),'token')
print(Token[0])

# Accept self sign certificate
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

#input values
url = urls.base_url + urls.Knowledge_Base_Types
auth = {"Authorization": "Bearer {}".format(Token[0])}

#Get response
response = requests.get(url, headers=auth, verify= False)

#Parse response to json response
json_response = json.loads(response.text)
print(json_response)