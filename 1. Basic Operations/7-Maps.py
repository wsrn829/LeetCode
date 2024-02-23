class Map:
    def __init__(self):
        self.items = {}

    # Adding a key-value pair
    def add(self, key, value):
        self.items[key] = value

    # Removing a key-value pair
    def remove(self, key):
        if key in self.items:
            del self.items[key]

    # Updating the value for a key
    def update(self, key, value):
        if key in self.items:
            self.items[key] = value

    # Checking if a key exists
    def key_exists(self, key):
        return key in self.items

    # Accessing the value for a key
    def get(self, key):
        return self.items.get(key)

    # Finding the number of key-value pairs
    def size(self):
        return len(self.items)

    # Looping over keys
    def loop_keys(self):
        for key in self.items:
            print(key)

    # Looping over values
    def loop_values(self):
        for value in self.items.values():
            print(value)

    # Looping over key-value pairs
    def loop_items(self):
        for key, value in self.items.items():
            print(key, value)

    # Copying a map
    def copy(self):
        new_map = Map()
        new_map.items = self.items.copy()
        return new_map

    # Merging two maps
    def merge(self, other_map):
        self.items.update(other_map.items)
