import requests
import pytest

# =====================   МЕТОДЫ REQUEST   ======================

# ===  GET     -  получить
# ===  POST    -  отправить
# ===  HEAD    -  возвразает заголовок и тело
# ===  PUT     -  создание
# ===  PATCH   - частичные изменения
# ===  DELETE
# ===  OPTIONS - запрос инф-ции

# C  create
# R  read
# U  update
# D  delete
# https://restful-booker.herokuapp.com/

base_url = "https://restful-booker.herokuapp.com/booking"
auth_url = "https://restful-booker.herokuapp.com/auth"

def test_get_code():
    result = requests.get(base_url)
    print(result)
    assert result.status_code

def test_get_booking_by_id():
    response = requests.get(f'{base_url}/1')
    response_data = response.json()
    expected_keys = [
            "firstname",
            "lastname",
            "totalprice",
            "depositpaid",
            "bookingdates",
            "additionalneeds"
    ]
    # print(response_data)
    assert response.status_code == 200
    print(response_data)
    print(len(response_data.keys))

    # проверить длину
    # assert len(expected_keys) == len(response_data.keys())
    assert len(response_data.keys()) == len(expected_keys)
    # for key in expected_keys:
    #     assert key in response_data.keys()


def test_create_booking():
    payload = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-02-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(base_url, json=payload)
    print(response.json()['bookingid'])
    assert response.status_code == 200

def test_check_created_booking():
    result = requests.get(f"{base_url}/2107")
    print(result.json())
    assert result.status_code == 200
    assert result.json()['firstname'] == "James"

def test_update_booking():
    payload = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-02-01"
        },
        "additionalneeds": "Lunch"
    }

    token = {"Cookie": "token=0283c7540a0f213"}

    response = requests.put(f'{base_url}/2107', json=payload, headers=token)
    assert response.status_code == 200
    response_2 = requests.get(f'{base_url}/2107')
    assert response_2.json()["additionalneeds"] == "Lunch"

def test_get_token():
    authdata = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(auth_url, json=authdata)
    token = response.json()["token"]
    print(token)
    assert response.status_code == 200