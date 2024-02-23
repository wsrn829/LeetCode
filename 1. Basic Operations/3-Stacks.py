class Stack:
    def __init__(self):
        self.items = []

    # Pushing an element onto the stack
    def push(self, item):
        self.items.append(item)

    # Popping an element from the stack
    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    # Peeking at the top element of the stack
    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    # Checking if the stack is empty
    def is_empty(self):
        return len(self.items) == 0

    # Finding the size of the stack
    def size(self):
        return len(self.items)

    # Copying the stack
    def copy(self):
        new_stack = Stack()
        new_stack.items = self.items.copy()
        return new_stack

    # Merging two stacks
    def merge(self, other_stack):
        self.items.extend(other_stack.items)

    # Loop over a stack
    def loop(self):
        for item in self.items:
            print(item)

    # Reverse a stack
    def reverse(self):
        self.items.reverse()

    # Convert a stack to an array or vice versa
    def to_array(self):
        return self.items

    @classmethod
    def from_array(cls, array):
        stack = cls()
        stack.items = array.copy()
        return stack

    # Sort a stack
    def sort(self):
        self.items.sort()

    # Find the maximum or minimum value in a stack
    def max(self):
        if not self.is_empty():
            return max(self.items)

    def min(self):
        if not self.is_empty():
            return min(self.items)

    # Find the sum of all items in a stack
    def sum(self):
        return sum(self.items)

    # Find the average of all items in a stack
    def average(self):
        return sum(self.items) / len(self.items)

    # Find the median of all items in a stack
    def median(self):
        sorted_items = sorted(self.items)
        length = len(sorted_items)
        if length % 2 == 0:
            return (sorted_items[length // 2 - 1] + sorted_items[length // 2]) / 2
        else:
            return sorted_items[length // 2]
