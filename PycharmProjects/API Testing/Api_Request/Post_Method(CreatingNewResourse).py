import  requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users"

# Read Input Json file
file = open('C:\\Users\\Pratik\\Desktop\\CreateUser.json')
json_input = file.read()
request_json = json.loads(json_input)

# Make POST Request with Json Input body
response = requests.post(url,request_json)

#  Validating response status code
assert response.status_code == 201

# Fetch Header from Response
print(response.headers.get('Content-Length'))

# Parse response into Json format
response_json = json.loads(response.text)

# Parse id using Json Path
id = jsonpath.jsonpath(response_json,'id')
print(id[0])