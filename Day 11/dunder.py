class Animal:
    def __new__(cls, name):
        print("__new__() is called")
        return object.__new__(cls)

    def __init__(self, name: str):
        print("__init__() is called")
        self.name = name

if __name__ == "__main__":
    cat = Animal("Layla")
    print(cat.name)