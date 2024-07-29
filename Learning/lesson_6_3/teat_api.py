# https://restful-booker.herokuapp.com/apidoc/index.html#api-Booking-GetBookings

import requests
import pytest

# # GET https://restful-booker.herokuapp.com/booking
#
# response = requests.get('https://restful-booker.herokuapp.com/booking')
# print(response.json())
# print(response.status_code)
# print(response.headers)
#
# # 404 not faund - endpoint pictures - не существует
# response = requests.get('https://restful-booker.herokuapp.com/pictures')
# print(response.status_code)

#  POST https://restful-booker.herokuapp.com/booking

def create_bookig(name, surname):
    url = "https://restful-booker.herokuapp.com/booking"
    data = {
    "firstname" : name,
    "lastname" : surname,
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"}

    response = requests.post(url=url, json=data)

    return response.json()

def get_booking_by_id(id_):
    # возвращаем конкретный id созданного booking
    url = f'https://restful-booker.herokuapp.com/booking/{id_}'

    response = requests.get(url)

    # print(response.json())

    return response.json()

# из бронирования с43 вытащили id с 44 и чечрез id вернули бронирование с 45
# booking = create_bookig()
# id_ = booking['bookingid']
# get_booking_by_id(id_)

@pytest.fixture()
def token():
    url = 'https://restful-booker.herokuapp.com/auth'

    data = {
        "username": "admin",
        "password": "password123"
    }

    response = requests.post(url=url, json=data)

    # на этот url вызвали данные
    print(response.json())    #{'token': '147f4d8d9d96d82'}

    # преобразовали ответ из json в ловарь и вытащили из него токен
    return response.json()['token']

# create_tocken()
# print(create_tocken())

def test_create_booking():
    name = 'Mike'
    surname = 'Simpson'

    booking = create_bookig(name=name, surname=surname)
    id = booking['bookingid']

    # print(booking)  #337

    new_booking = get_booking_by_id(id)

    # print(new_booking)

    assert new_booking['firstname'] == name
    assert new_booking['lastname'] == surname


# лучше всего создавать заново токен чтобы не падали тесты, т.к мы не знаем
# сколько времени хранится токен
# поэтому создаем токен внутри теста чтобы он постоянно его возвращал

def test_create_and_patch(token):
    name = 'Mike'
    surname = 'Simpson'
    new_name = 'Jhon'
    new_surme = 'Smith'

    booking = create_bookig(name=name, surname=surname)
    id = booking['bookingid']

    url = f'https://restful-booker.herokuapp.com/booking/{id}'

    headers = {'Cookie': f'token={token()}'}

    new_data = {
    "firstname" : new_name,
    "lastname" : new_surme}

    response = requests.patch(url, headers=headers, json=new_data)
    result = response.json()

    assert result['firstname'] == new_name
    assert result['lastname'] == new_surme
