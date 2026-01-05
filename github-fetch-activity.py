# https://api.github.com/users/<username>/events

import requests, json

username = input('Enter your github username: ')

url = f"https://api.github.com/users/{username}/events/public"

response = requests.get(url)

if response.status_code == 200:
    print('Request was sucessful')
    data = response.json()
else:
    print('Request failed')

for thing in data:
    event_type = thing['type']

    event_actor = thing['actor']['login']

    event_repo = thing['repo']['name']

    print(f'{event_actor} did a {event_type} on {event_repo}')
    print()



