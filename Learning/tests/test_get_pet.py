import random
from pprint import pprint
import requests

# для вызова test_assert.py - тем самым поломали все остальное
dct = {
    "base_url": "https://petstore.swagger.io/v2/",
    "get_pet": "/pet/",
    "create_pet": "/pet"
}

# full_url = base_url + get_pet_by_iu_url
# response = requests.get(full_url)
# print(response)
#
#
# def test_get_pet_by_id():
#     response = requests.get(full_url)
#     status_code = response.status_code
#     body = response.json()
#     print(status_code)
#     print(body)

def test_create_pet():
    full_url = base_url + create_pet
    pet_id = random.randint(10000, 100000)
    with open("id.txt", "w", encoding="utf-8") as f:
        f.write(f"{pet_id}")
    data = {
        "id": pet_id,
        "category": {
            "id": 2,
            "name": "Olga"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    # full_url1 = base_url + get_pet_by_iu_url + "123456789"
    response = requests.post(full_url, json=data)
    print()
    # status_code = response.status_code
    # print(status_code)
    body = response.json()
    print(body)
#   статус 200 - это значит баг, д.б. 201
    print("==================================")

    # or

    full_url1 = f"{base_url}{get_pet_by_iu_url}{pet_id}"
    response1 = requests.get(full_url1)
    print(response1.json())

# для получения id
# def test_update_pet():
#     pass

def test_update_pet():
    full_url = base_url + create_pet
    with open("id.text", "r", encoding="utf-8") as f:
        pet_id = f.readline().strip()
        data = {
            "id": pet_id,
            "category": {
                "id": 2,
                "name": "Olga F"
            },
            "name": "scotish",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": "available"
        }
        response = requests.put(full_url, json=data)
        data = response.json()
        print()
        print("============================================")
        pprint(data)

        full_url1 = f"{base_url}{get_pet_by_iu_url}{pet_id}"
        response1 = requests.get(full_url1)
        pprint(response1.json())

# def test_delete_pet():
#     pass

def test_delete_pet():
    with open("id.text", "r", encoding="utf-8") as f:
        pet_id = f.readline().strip()
    full_url = f"{base_url}{get_pet_by_iu_url}{pet_id}"
    response = requests.delete(full_url)
    print()
    print("============================================")
    pprint(response.json())
    full_url1 = f"{base_url}{get_pet_by_iu_url}{pet_id}"
    response1 = requests.get(full_url1)
    print(response1.json())