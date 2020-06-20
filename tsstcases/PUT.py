import requests
import json
import jsonpath

# api url
url = "https://reqres.in/api/users/2"
#read input json file
file=open('C:\\Users\\VIJAYA\\OneDrive\\Documents\\api\\put.txt','r')
json_input = file.read()
request_json = json.loads(json_input)
# make put request with json input body
response = requests.put(url,request_json)
# fetch response code
print(response.status_code)
#assert  response.status_code == 200

#parse response content
response_json= json.loads(response.text)
updated_li  =jsonpath.jsonpath(response_json,'updatedAt')
print(updated_li[0])


