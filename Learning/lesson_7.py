def get_name():
    name = input("Enter your name: ")
    # print(name)
    return name

def say_hello():
    name = get_name()
    print(f"Hello {name}")

say_hello()