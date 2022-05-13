
import requests
import json
import jsonpath

#get rid-off ssl exceptions
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

#input values
url = "https://<ServerIP/FQDN>/LiveTime/services/v1/auth/login"
file = open("C:\\Users\\DPratap\\Desktop\\PythonAPI\\ZSDAPIAutomation\\data.json", 'r')
json_input = file.read()
request_json = json.loads(json_input)
print(request_json)


#Get response
response = requests.post(url,json=request_json,verify= False)

#Parse response to json response
json_response = json.loads(response.text)
print(json_response)

# get all property values
client_id = jsonpath.jsonpath(json_response,'clientId')
full_name = jsonpath.jsonpath(json_response,'fullName')
msg = jsonpath.jsonpath(json_response,'message')
Token = jsonpath.jsonpath(json_response,'token')

# Print all the property values
print((client_id[0]))
print((full_name[0]))
print((msg[0]))
print((Token[0]))

# Compare Expected values with Actual values
assert response.status_code == 200
assert client_id[0] == 12
assert full_name[0] == 'Yashwanth Bellur'
assert msg[0] == 'Login Successful.'



