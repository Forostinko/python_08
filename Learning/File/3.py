file_name = "answer1.txt"

with open(file_name, "r", encoding="utf-8") as f:
    content = [i.strip() for i in f.readline()]
    print(content)

for i in content:
    print(i)
