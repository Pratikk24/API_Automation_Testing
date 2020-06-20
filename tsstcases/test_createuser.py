import requests
import json
import jsonpath

# api url
url = "https://reqres.in/api/users"

def test_create_new_user():
    #read input json file
    file = open('C:\\Users\\VIJAYA\\OneDrive\\Documents\\api\\create.txt','r')
    json_input = file.read()
    request_json =  json.loads(json_input)
    #make post request with json input body
    response = requests.post(url,request_json)
    #validating response code
    assert  response.status_code == 201
    #fetch header from response
    print(response.headers.get('Content-Length'))
    #parse response to json format
    response_json = json.loads(response.text)

