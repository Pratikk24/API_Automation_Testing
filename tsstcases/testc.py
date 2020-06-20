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
    response = requests.post(url,request_json)
    assert  response.status_code == 201


def test_create_other_user():
    #read input json file
    file = open('C:\\Users\\VIJAYA\\OneDrive\\Documents\\api\\New Text Document.txt','r')
    json_input = file.read()
    request_json =  json.loads(json_input)
    response = requests.post(url,request_json)
    response_json = json.loads(response.text)
    id = jsonpath.jsonpath(response_json,'id')
    print(id[0])