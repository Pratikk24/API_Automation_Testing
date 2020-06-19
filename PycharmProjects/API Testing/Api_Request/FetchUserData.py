import requests

# API URL
url = "http://claim-portal-bajaj-dev.qa.i3systems.in/#/claims?profile_id=1&limit=20&offset=0"

# Send Get Request
response = requests.get(url)
print(response)

# Display Response Content
print(response.content)




