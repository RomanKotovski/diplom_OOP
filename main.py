import requests
import json
from datetime import datetime
import yadisk
import time
from tqdm.auto import tqdm

class VK:

   def __init__(self, token_VK, user_id, version='5.131'):
       self.token = token_VK
       self.user_id = user_id
       self.version = version
       self.params = {'access_token': self.token, 'v': self.version}

   def users_info(self):
       url = 'https://api.vk.com/method/photos.get'
       params = {'owner_id': user_id, 'album_id': 'profile', 'album_id': 'profile', 'extended': '1'}
       response = requests.get(url, params={**self.params, **params})
       return response.json()

class Ya:
    def __init__(self, file_path, token: str):
        self.token = token
        self.file_path = file_path
    def upload_file():
        yadisk.YaDisk(token=token).mkdir(f'/{user_id}') #создаем новую папку
        link = VK(token_VK, user_id).users_info()
        data_photo = link['response']['items']
        count = 0  # счетчик для количества фото, по умолчанию 5
        name_list = []  # список имен для поиска повторений
        file_list = []  # итоговый список имен и размеров фото
        for data in tqdm(data_photo, 'Загрузка фото', total=5):
            if count < 5:
                time.sleep(0.2)
                name_photo =  str(data['likes']['count'])
                if name_photo in name_list:
                    name_photo += f" {str(datetime.fromtimestamp(data['date']))}" # в случае повторения имени добавляем дату
                name_list.append(name_photo)
                sizes_photo = data['sizes']
                max_size = 0
                for size in sizes_photo:
                    if size['height'] >= max_size:
                        max_size = size['height']
                for size in sizes_photo:
                    if size['height'] == max_size:
                        link_photo = size['url']
                        file_list.append({'name': name_photo, 'size': size['type']})
                        yadisk.YaDisk(token=token).upload_url(link_photo, f'/{user_id}/{name_photo}.jpg') #загружаем фото в нужную папку
                count += 1
            else:
                break # при достижении порогового значения прерываем цикл
        json_list = json.dumps(file_list)
        with open("file_list.json", "w") as file_info:
            file_info.write(json_list)

if __name__ == '__main__':
    token_VK = str(input('Введите ваш токен VK: ')) #токен вк
    user_id = str(input('Введите id пользователя VK: ')) #юсерайди вк
    token = str(input('Введите ваш токен ЯндексДиск: '))   #токен яндекса
    Ya.upload_file()