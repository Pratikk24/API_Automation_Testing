import  requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users/2"

# Read Input Json file
file = open('C:\\Users\\Pratik\\Desktop\\CreateUser.json')
json_input = file.read()
request_json = json.loads(json_input)

# Make PUT Request with Json Input body
response = requests.put(url,request_json)

#  Validating response status code
assert response.status_code == 200

# Parse response content
response_json = json.loads(response.text)
updated_li = jsonpath.jsonpath(response_json,'updatedAt')
print(updated_li[0])