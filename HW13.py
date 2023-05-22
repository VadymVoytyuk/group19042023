import requests
from pprint import pprint

url = 'https://dummyjson.com/users?skip=0&limit=100'

response = requests.get(url)
# print(response.content)
# pprint(response.json())
data = response.json()
# pprint(data)
users = data['users']
# pprint(users)
total_brown_hair_age = 0
total_brown_hair_age_man = 0

for user in users:
    if user['hair']['color'] == 'Brown' and user['gender'] == 'male':
        # print(user)
        total_brown_hair_age += user['age']
        total_brown_hair_age_man += 1

if total_brown_hair_age_man:
    print(f'Average age for Brown hair male is : {(total_brown_hair_age / total_brown_hair_age_man)}')

    for user in users:
        if user['address'].get('city', '') == 'Louisville':
            print(user['firstName'], user['lastName'], 'is Louisville citizen')
