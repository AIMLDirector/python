d1 = { 1: "one", 2: "two", 3: "three"}
print(type(d1))
print(d1[1])

x= d1.keys()
print(x)
y= d1.values()
print(y)
d1[4] = "four"
print(d1)
d1.popitem()
print(d1)
d1.pop(2)
print(d1)
for x in d1.keys():
    print(x)

for y in d1.values():
    print(y)

for x,y in d1.items():
    print(x,":", y)

#d1.clear()
#print(d1)
import json

jsondata = json.dumps(d1)
print(type(jsondata))
print("converted dict to json:", jsondata)

import yaml
yamldata = yaml.dump(d1)
print(yamldata)

with open('student.yaml', 'r') as yamlfile:
    #print(yamlfile.read())
    ydata = yaml.safe_load(yamlfile)
    print(ydata.College)



