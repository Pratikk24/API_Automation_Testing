import requests
import json
import jsonpath



# API URL
url = "https://reqres.in/api/users?page=2"

#SEND GET REQUEST

response = requests.get(url)
# DISPLAY RESPONSE CONTENT
#print(response.content)
#print(response.headers)

# parse response to json format
json_response = json.loads(response.text)
#print(json_response)
#  fetch value using json path
pages = jsonpath.jsonpath(json_response,'total_pages')
#print(pages[0])
assert pages[0] == 2
