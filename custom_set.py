





class CustomSet:
    def __init__(self): 
        self.items = set()

    def add:(self, item):
        self.items.add(item)

    def remove(self, item):
        self.items.remove(item)

    def as_list(self):
        return list(self.items)


    def clear:
        self.items.clear()

def main()-> None:
    my_set = CustomSet()
    my_set.add("dog")
    my_set.add("cat")
    my_set.add("rabbit")


    print(my_set.as_list()) # ["dog", "cat", "rabbit"]


    my_set.remove("cat")
    print(my_set.as_list()) # ["dog", "rabbit"]


    try: 
        my_set.remove("fox")
    except KeyError:
        print("Item not removed, moving forward")

    my_set.clear()
    print(my_set.as_list()) # []


if __name__ == "__main__": 
    main()


