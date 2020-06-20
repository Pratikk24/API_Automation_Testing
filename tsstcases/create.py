import requests
import json
import jsonpath

#api url
url = "https://reqres.in/api/users"

#read import json file
file = open('C:\\Users\\VIJAYA\\OneDrive\\Documents\\api\\create.txt','r')
json_input = file.read()
request_json = json.loads(json_input)

#print(request_json)

# make post request with json input body
response = requests.post(url,request_json)
#print(response.content)

# validating response code
assert response.status_code == 201
# fetch header from response
print(response.headers)
# parse response content
response_json= json.loads(response.text)
#updated_li = jsonpath.jsonpath(response_json,'updatedAt')
#print(updated_li[0])