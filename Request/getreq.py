import config
import requests

#print(config.users())
#print(config.access_token())
url = config.users()
r = requests.get(url)
print(r.status_code)
print(r.text)
print(r.url)
print(r.json())