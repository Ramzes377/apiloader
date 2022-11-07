import os

from api.loader import get_raw_data, write_data
from api.drive import upload_data

test_api_urls = [
    'https://api.publicapis.org/entries',
    'https://catfact.ninja/fact',
    'https://api.coindesk.com/v1/bpi/currentprice.json'
]

for i, url in enumerate(test_api_urls, start=1):
    data = get_raw_data(url)

    filename = f'api-data-{i}'
    filepath = write_data(filename, data)

    upload_data(filepath, filename=f'{filename}.txt')

    os.remove(filepath)
