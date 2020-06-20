import requests
import json
import jsonpath

#api url
url = "https://reqres.in/api/users"

#read import json file
file = open('C:\\Users\\VIJAYA\\OneDrive\\Documents\\api\\create.txt','r')
json_input = file.read()
request_json = json.loads(json_input)

print(request_json)

# make post request with json input body
response = requests.post(url,request_json)
print(response.content)