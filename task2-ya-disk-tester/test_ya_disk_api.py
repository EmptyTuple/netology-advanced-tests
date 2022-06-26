import requests
import unittest
import re


class YaDiskTest(unittest.TestCase):
    '''Тестовый класс для прямого теста создания папки на YandexDisk.
       В аттрибуте "token_file" укажите имя файла, содержащего токен и путь к нему есои необходимо.'''
    
    token_file = 'task2-ya-disk-tester/yat.txt'
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    folder_name = 'test'
    with open(token_file, 'r', encoding='utf-8') as file:
        token = file.read().strip()
    HEADERS = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {token}'
        }   
    params = {"path": folder_name}
    
    def test_empty_token(self):
        '''Проверяем, что считываемый токен - непустая строка.'''
        self.assertNotEqual(self.token, '')
    
    def test_token_symbols(self):
        '''Проверяем, что токен не имеет запрещенных символов.'''
        pattern = r'^[a-zA-Z0-9-]+'
        self.assertEqual(self.token, re.match(pattern, self.token)[0])

    def test_connect(self):
        '''Проверяем наличие соединения'''
        res = requests.get('https://cloud-api.yandex.net/v1/disk/', headers=self.HEADERS)
        self.assertEqual(res.status_code, 200)
  
    def test_create_folder(self):
        '''Проверяем код ответа 201 при создании дирекории на YandexDisk.'''
        res = requests.put(self.url, headers=self.HEADERS,
                           params=self.params)
        self.assertEqual(res.status_code, 201)

    def test_exist_folder(self):
        '''Проверяем, что директория с заданным именем есть на YandexDisk.'''
        res = requests.get(self.url, headers=self.HEADERS,
                           params=self.params)
        self.assertEqual(res.status_code, 200)
    
# Возможные отрицательные тесты на ошибки:
    def test_folder_409(self):
        '''Проверяем код ответа 409 при создании дирекории на YandexDisk.'''
        res = requests.put(self.url, headers=self.HEADERS,
                           params=self.params)
        self.assertEqual(res.status_code, 409)
            
    def test_folder_404(self):
        '''Проверяем код ответа 409 при создании дирекории на YandexDisk.'''
        res = requests.get(self.url, headers=self.HEADERS, params=self.params)
        self.assertNotEqual(res.status_code, 404)

    def test_delete_folder(self):
        '''Тестирование удаления директории.'''
        res = requests.delete(self.url, headers=self.HEADERS,
                               params=self.params)
        self.assertEqual(res.status_code, 204)


if __name__ == '__main__':
    tester = YaDiskTest()
    tester.test_empty_token()
    tester.test_token_symbols()
    tester.test_create_folder()
    tester.test_exist_folder()
    tester.test_folder_409()
    tester.test_folder_404()
    tester.test_delete_folder()
    


