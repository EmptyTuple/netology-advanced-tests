import requests

class YaDiskFolderHandler:
    base_url = 'https://cloud-api.yandex.net/v1/disk/resources'
    token_file = 'task2-ya-disk-tester/yat.txt' 

    def get_token(self, token_file: str) -> str:
        with open(self.token_file, 'r', encoding='utf-8') as file:
            return file.read().strip()

    def create_folder(self, folder_name: str, url: str = base_url) -> str:
        HEADERS = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.get_token(self.token_file)}'
        }
        
        params = {"path": folder_name}
        res = requests.put(url, headers=HEADERS,
                            params=params)
        print(res.status_code)
        return res

    def get_folder(self, folder_name: str, url: str = base_url) -> str:
        HEADERS = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.get_token(self.token_file)}'
        }
        
        params = {"path": folder_name}
        res = requests.get(url, headers=HEADERS,
                            params=params)
        return res

    def delete_folder(self, folder_name: str, url: str = base_url) -> str:
        HEADERS = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.get_token(self.token_file)}'
        }
        
        params = {"path": folder_name}
        res = requests.delete(url, headers=HEADERS,
                               params=params)
        print(res.status_code)
        return res

if __name__ == '__main__':
    ya = YaDiskFolderHandler()
    ya.create_folder('testf')
    print(ya.get_folder('testf'))
    ya.delete_folder('testf')
