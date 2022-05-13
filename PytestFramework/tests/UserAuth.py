#API Url
import requests
import json
import jsonpath
from PytestFramework.conf import urls;
from PytestFramework.data.JsonData import UserPostData

#get rid-off ssl exceptions
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

#input values
url = urls.base_url + urls.login
jsonData = json.loads(UserPostData)

#Get response
response = requests.post(url,json=jsonData,verify= False)

#Parse response to json response
def userLogin():
    json_response = json.loads(response.text)
    return json_response

# get all property values
client_id = jsonpath.jsonpath(userLogin(),'clientId')
full_name = jsonpath.jsonpath(userLogin(),'fullName')
msg = jsonpath.jsonpath(userLogin(),'message')
Token = jsonpath.jsonpath(userLogin(),'token')

#Print all the property values
print((client_id[0]))
print((full_name[0]))
print((msg[0]))
print((Token[0]))

# Compare Expected values with Actual values
assert response.status_code == 200
assert client_id[0] == 5
assert full_name[0] == 'Yashwanth Bellur'
assert msg[0] == 'Login Successful.'



