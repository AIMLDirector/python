import config
import requests
from requests.exceptions import Timeout

url = config.users() +"7204707"
headers =dict()
headers['Authorization']= 'Bearer ' + config.access_token()
r = requests.delete(url, headers=headers)
print(r.status_code)
#print(r.json())
