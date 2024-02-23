class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    # Loop over key-value pairs
    def loop(self):
        for item in self.table:
            if item:
                for key, value in item:
                    print(key, value)

    # Find the value for a key
    def find(self, key):
        index = hash(key) % self.size
        if self.table[index]:
            for k, v in self.table[index]:
                if k == key:
                    return v

    # Insert a key-value pair
    def insert(self, key, value):
        index = hash(key) % self.size
        if not self.table[index]:
            self.table[index] = []
        self.table[index].append((key, value))

    # Update the value for a key
    def update(self, key, value):
        index = hash(key) % self.size
        if self.table[index]:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    self.table[index][i] = (key, value)
                    return

    # Check if a key has been used
    def key_exists(self, key):
        index = hash(key) % self.size
        if self.table[index]:
            for k, v in self.table[index]:
                if k == key:
                    return True
        return False

    # Delete a key-value pair
    def delete(self, key):
        index = hash(key) % self.size
        if self.table[index]:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    del self.table[index][i]
                    return

    # Search for a value
    def value_exists(self, value):
        for item in self.table:
            if item:
                for k, v in item:
                    if v == value:
                        return True
        return False

    # Get all keys or values
    def get_keys(self):
        keys = []
        for item in self.table:
            if item:
                for k, v in item:
                    keys.append(k)
        return keys

    def get_values(self):
        values = []
        for item in self.table:
            if item:
                for k, v in item:
                    values.append(v)
        return values

    # Get the number of key-value pairs
    def size(self):
        count = 0
        for item in self.table:
            if item:
                count += len(item)
        return count

    # Check if a hash table is empty
    def is_empty(self):
        for item in self.table:
            if item:
                return False
        return True

    # Clear a hash table
    def clear(self):
        self.table = [None] * self.size

    # Copy a hash table
    def copy(self):
        new_table = HashTable(self.size)
        for item in self.table:
            if item:
                for k, v in item:
                    new_table.insert(k, v)
        return new_table

    # Merge two hash tables
    def merge(self, other_table):
        for item in other_table.table:
            if item:
                for k, v in item:
                    self.insert(k, v)

    # Convert a hash table to an array or vice versa
    def to_array(self):
        array = []
        for item in self.table:
            if item:
                for k, v in item:
                    array.append((k, v))
        return array

    @classmethod
    def from_array(cls, array, size=10):
        table = cls(size)
        for k, v in array:
            table.insert(k, v)
        return table

    # Sort a hash table by keys or values
    def sort(self, by_key=True):
        sorted_table = sorted(self.to_array(), key=lambda x: x[0] if by_key else x[1])
        return HashTable.from_array(sorted_table, self.size)

    # Find the maximum or minimum key or value
    def max_key(self):
        max_key = None
        for item in self.table:
            if item:
                for k, v in item:
                    if max_key is None or k > max_key:
                        max_key = k
        return max_key

    def min_key(self):
        min_key = None
        for item in self.table:
            if item:
                for k, v in item:
                    if min_key is None or k < min_key:
                        min_key = k
        return min_key

    def max_value(self):
        max_value = None
        for item in self.table:
            if item:
                for k, v in item:
                    if max_value is None or v > max_value:
                        max_value = v
        return max_value

    def min_value(self):
        min_value = None
        for item in self.table:
            if item:
                for k, v in item:
                    if min_value is None or v < min_value:
                        min_value = v
        return min_value

    # Find the average of all values
    def average(self):
        total = 0
        count = 0
        for item in self.table:
            if item:
                for k, v in item:
                    total += v
                    count += 1
        return total / count
