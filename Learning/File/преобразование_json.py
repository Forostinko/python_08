import json
import os.path

json_file = """
    {
        "key1": 1,
        "key2": 2
    }
    """
# json.dumps() - преобразует обьект в строку в формате json
# json.dump()  - преобразует обьект в строку и записывает в файл

# json.load()  - преобразует json-файл в питоновский обьект
# json.loads() - преобразует json-строку в питоновский обьект

json_file1=json.loads(json_file)
print(type(json_file1))
print(json_file)
print(json_file1["key1"])

dct = {
    "name": "Olga",
    "age": 18,
    "profession": "QA"
}
json_file = json.dumps(dct)
print(type(dct))
print(dct)
print("=========================================")
print(type(json_file))
print(json_file)

# Создался файл
file_name = "json.json"
with open(file_name, "w") as f:
    json.dump(dct, f)


with open(file_name, "r") as f:
    a = json.load(f)

for key, value in a.items():
    print(key, value)


# покажет путь к файлу
def return_file_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, file_name)
    print(file_path)

return_file_path(file_name)
