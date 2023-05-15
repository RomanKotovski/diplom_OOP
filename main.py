import requests
import json
from pprint import pprint
import sys
import time
import yadisk


class VK:

   def __init__(self, token_VK, user_id, version='5.131'):
       self.token = token_VK
       self.id = user_id
       self.version = version
       self.params = {'access_token': self.token, 'v': self.version}

   def users_info(self):
       url = 'https://api.vk.com/method/photos.get'
       params = {'user_ids': self.id, 'album_id': 'profile', 'extended': '1'}
       response = requests.get(url, params={**self.params, **params})
       return response.json()


class Ya:
    def __init__(self, file_path, token: str):
        self.token = token
        self.file_path = file_path
    def upload_file():
        link = VK(token_VK, user_id).users_info()
        data_photo = link['response']['items']
        count = 0
        for data in data_photo:
            if count < 5:
                time.sleep(1)
                name_photo = str(data['likes']['count'])
                sizes_photo = data['sizes']
                for size in sizes_photo:
                    if size['type'] == 'w':
                        link_photo = size['url']
                pprint(link_photo)
                y = yadisk.YaDisk(token=token).upload_url(link_photo, name_photo)
                count += 1
            else:
                break


token_VK = 'vk1.a.GZCJaTIESuUoq_yF0AATelZlf2xpQkrozlQXRGDQdT2odtDMd7ZtHJuZVgXdiCR646SeLJxJlS9NBuNzufbUPWjiuiyWmMxjZ9HdfCqgN1p2XUdISKVxm8kQZfZzrWrWV3_IDQ4_hB4WcUWKwWztqiQas-4AIxZSOlmIjn0LBKKWm4OWykzUhcvq2RqOJ6-xuyqNZSmHmSE1iipYI8aLRQ'
user_id = '64870295'
token = 'y0_AgAAAAAzTKoOAADLWwAAAADirnYaBAZfFooQRhSQlYuCtLWT-UTLq6U'   #токен
Ya.upload_file()