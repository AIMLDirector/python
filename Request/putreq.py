import config
import requests

url = config.users() +"7204397"
headers =dict()
headers['Authorization']= 'Bearer ' + config.access_token()

data = dict()
data['name'] ='kumar'

r = requests.put(url,data=data, headers=headers)
print(r.json())