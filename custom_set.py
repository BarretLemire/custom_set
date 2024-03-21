class CustomSet:
    def __init__(self):
        self.items = []

    def add(self, item):
        if item not in self.items:
            self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            raise KeyError("Item not found in the set")

    def as_list(self):
        return self.items

    def clear(self):
        self.items = []

def main():
    my_set = CustomSet()
    my_set.add("dog")
    my_set.add("cat")
    my_set.add("rabbit")

    print(my_set.as_list())  # ["dog", "cat", "rabbit"]

    my_set.remove("cat")
    print(my_set.as_list())  # ["dog", "rabbit"]

    try:
        my_set.remove("fox")
    except KeyError:
        print("Item not removed, moving forward")

    my_set.clear()
    print(my_set.as_list())  # []

if __name__ == "__main__":
    main()
