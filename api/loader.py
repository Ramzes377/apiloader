import requests
import os

load_path = './api/data/'

try:
    os.mkdir(load_path)
except FileExistsError:
    pass


def get_raw_data(url: str) -> dict:
    r = requests.get(url)
    return r.json()


def write_data(filename: str, data: dict) -> str:
    save_path = os.path.join(load_path, filename)
    with open(save_path, 'w') as file:
        file.write(str(data))
    return save_path
