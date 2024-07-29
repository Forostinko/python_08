import requests

username = "forostinko"
password = "test123"

auth = requests.request(method="POST", url="https://dev.epm.polymatica.ru/api/v1/manager/auth",
                        json={"is_remember":True,
                              "username":username,
                              "password":password})
assert auth.status_code == 200
key = auth.json()
print(key)
token = key['access_token']

create_project = requests.request(method="POST",
                                  url="https://dev.epm.polymatica.ru/api/v1/epm/projects",
                                  json={"key": "create_project",
                                        "name": "Create_project",
                                        "description": "",
                                        "user_id": 387},
                                  headers={"authorization": f"Bearer {token}"})
# assert 1 == 1
create_project

rename_project = requests.request(method="PATCH",
                                  url="https://dev.epm.polymatica.ru/api/v1/epm/projects",
                                  json={"key": "create_project",
                                        "name": "rename_project1",
                                        "description": ""},
                                  headers={"authorization": f"Bearer {token}"})

if rename_project.status_code == 200:
    print("Проект успешно обновлен")
else:
    print("Возникла ошибка при обновлении проекта")
    print(rename_project.text)
rename_project

delete_project = requests.request(method="DELETE",
                                  url="https://dev.epm.polymatica.ru/api/v1/epm/projects/create_project",
                                  headers={"authorization": f"Bearer {token}"})

if delete_project.status_code == 200:
    print("Проект удален")
else:
    print("Ошибка")
delete_project





