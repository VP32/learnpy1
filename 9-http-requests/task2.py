import os.path

import requests


class YaUploader:
    HOST = 'https://cloud-api.yandex.net:443'

    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загруджает файл file_path на яндекс диск"""
        resp_url = requests.get(
            self.HOST + "/v1/disk/resources/upload",
            params={"path": os.path.basename(file_path), "overwrite": True},
            headers={"Authorization": "OAuth " + self.token}
        )
        resp_url.raise_for_status()

        with open(file_path, "rb") as f:
            resp_upload = requests.put(resp_url.json()["href"], f)
            resp_upload.raise_for_status()

        return resp_upload.status_code


uploader = YaUploader('--ваш токен--')
result = uploader.upload(os.path.join("files", "DSC07566_.jpg"))
print(f"Файл загружен со статусом: {result}")
