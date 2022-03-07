import requests
from pprint import pprint
url = 'https://backend-assignment-reunion.herokuapp.com/api/authenticate/'
myobj = {
    "email": "demouser@sagargajare.in",
    "password": "demouser"
}

x = requests.post(url, data=myobj)

pprint(x.json())
token = x.json()['access_token']
print(token)
headers = {"content-type": "application/json; charset=UTF-8",
           'Authorization': 'JWT {}'.format(token)}
x = requests.get("https://backend-assignment-reunion.herokuapp.com/api/post/",
                 headers=headers)
pprint(x.json())
