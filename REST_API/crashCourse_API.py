import requests
import json


r = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

print(r.json())
print(type(r.json()['items']))

for i in r.json()['items']:
    print(i)

