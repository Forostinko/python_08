file_name = "answer.txt"

# file = open("file_name", "r", encoding="utf-8")
# # content = file_read()
# content = file.readline()
# # strip = удаляет переносы в начале и в конце
# print(content.strip())
# file.close()

# file = open("file_name", "r", encoding="utf-8")
# content = file.readline()
# while content != "":
#     print(content.strip())
#     content = file.readline()
# file.close()

# file = open("file_name", "r", encoding="utf-8")
# for i in file:
#     print(i.strip())
# file.close()

file = open("file_name", mode="r", encoding="utf-8")
content = []
for i in file.readline():
    content.append(i.strip())
print(content)
file.close()