import requests

user = 'forostinko'
password = 'test123'
auth = requests.request(method='post', url='https://dev.epm.polymatica.ru/api/v1/manager/auth',
                        json={"username": user,
                              "password": password,
                              "is_remember": False}
                        )
assert auth.status_code == 200
# assert auth.status_code == 204, 'Получен не успешный статус'
# response = auth.json()
# token = response['access_token']

sourses = requests.request(method='GET', url='http://192.168.10.204:11180/proxy/manager/api/v1/data-source')
assert sourses.status_code == 401
# assert sourses.status_code == 200, 'Получен неуспешный статус'


response = auth.json()
token = response['access_token']

sourses = requests.request(method='GET',
                           url='http://192.168.10.204:11180/proxy/manager/api/v1/data-source',
                           headers={'Authorization': f'Bearer {token}'})
assert sourses.status_code == 200
sourses = sourses.json()
# assert len(sourses['row']) == 3


