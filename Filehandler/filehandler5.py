import csv
import json
data = {}
with open('state_us.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        key = row["State"]
        data[key] = row


with open('StateUS.json', 'w', encoding='utf-8') as jsonfile:
    jsonfile.write(json.dumps(data))  # dump is to convert python object to string --  any action - split ,delete, sort ,filter ,or regular expression we need to use dump 

with open('StateUS.json') as file:
    data = json.load(file) #  json strng to  python object
    print(data)





 