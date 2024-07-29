from pprint import pprint

import requests
from tests.test_get_pet import dct

base_url = dct['base_url']
get_pet_by_id_url = dct['get_pet']
create_pet = dct['create_pet']


def test_get_pet_by_id():
    #     pass
    with open("id.txt", "r", encoding="utf-8") as f:
        pet_id = f.readline().strip()
    full_url = f'{base_url}{get_pet_by_id_url}{pet_id}'
    response = requests.get(full_url)
    status_code = response.status_code
    assert status_code == 200, f'Unexpected status code. Expect: {200}, Actual: {status_code}'
    # assert status_code == 201, f'Unexpected status code. Expect: {200}, Actual: {status_code}'
