import config
import requests

url = config.users()
name = input("Enter your Name: ")
email = input("Enter your email: ")
status = input("Enter your status: ")
gender = input("Enter your Gender: ")
data = dict()
data['name'] = name
data['email'] = email
data['status'] = status
data['gender']= gender
headers =dict()
headers['Authorization']= 'Bearer ' + config.access_token()
print(config.access_token())
print(data)
r = requests.post(url , data=data, headers=headers)
print(r.json())
