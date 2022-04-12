import os

import requests


class VkUser:
    URL = 'https://api.vk.com/method/'

    def __init__(self, id, token, version):
        self.id = id
        self.token = token
        self.version = version
        self.params = {
            'access_token': self.token,
            'v': self.version
        }

    def get_friends(self):
        request_params = {
            'user_id': self.id,
            'count': 1000
        }
        friends_resp = requests.get(self.URL + 'friends.get', {**self.params, **request_params})
        friends_resp.raise_for_status()
        return friends_resp.json()['response']['items']

    def get_both_friends(self, other):
        if type(other) is not VkUser:
            return 'wrong data type'

        friends1 = self.get_friends()
        friends2 = other.get_friends()

        intersected = set(friends1).intersection(set(friends2))
        result = []
        for id in intersected:
            result.append(VkUser(id, self.token, self.version))

        return result

    def __str__(self):
        request_params = {
            'user_ids': self.id,
            'fields': 'screen_name'
        }
        info_resp = requests.get(self.URL + 'users.get', {**self.params, **request_params})
        info_resp.raise_for_status()
        screen_name = info_resp.json()['response'][0]['screen_name']
        return f'https://vk.com/{screen_name}'

    def __and__(self, other):
        if type(other) is not VkUser:
            return 'wrong data type'

        return self.get_both_friends(other)


with open(os.path.join('token', 'token.txt'), 'r') as f:
    token = f.read().strip()

with open(os.path.join('token', 'users.txt'), 'r') as f:
    users = f.read().strip().split(';')

user1 = VkUser(users[0], token, '5.131')
user2 = VkUser(users[1], token, '5.131')

common_friends = user1 & user2
for friend in common_friends:
    print(friend)
