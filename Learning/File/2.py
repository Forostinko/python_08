# Создание файла

file_name = "answer1.txt"

file = open(file_name, mode="w", encoding="utf-8")
file.write("Hello")
file.close()

# Добавление Hello
file = open(file_name, mode="a", encoding="utf-8")
file.write("Hello Hello")
# file.write("\nHello Hello")
file.close()