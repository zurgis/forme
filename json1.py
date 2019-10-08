import json

people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "666-666-6666",
            "emails": ["johnsmith@email.com", "john.smith@email.com"],
            "has_license": false
        },
        {
            "name": "Dean Winchester",
            "phone": "666-666-6666",
            "emails": null,
            "has_license": true
        }
    ]
}
'''

#data = json.loads(people_string)

#for person in data['people']:
#    #print(person['name'])
#    del person['phone']

#new_string = json.dumps(data, indent=2, sort_keys=True)

#print(new_string)

#with open('people.json', 'w') as f:
#    json.dump(data, f, indent=2) # Записывает данные, indent - отступ

with open('people.json', 'r') as f:
    data = json.load(f) # Считывает данные

for i in data['people']:
    print(i['name'], i['emails'])