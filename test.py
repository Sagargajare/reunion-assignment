import requests
from pprint import pprint
url = 'http://localhost:8000/api/authenticate/'
myobj = {
    "email": "demouser@sagargajare.in",
    "password": "demouser"
}

x = requests.post(url, data=myobj)

pprint(x.json())
token = x.json()['access_token']
print(token)
headers = {"content-type": "application/json; charset=UTF-8",
           "Authorization": "Bearer {}".format(token),
           "X-Auth-Token": token}
print(headers)
x = requests.get("http://localhost:8000/api/post",
                 headers=headers)
pprint(x.json())
