from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    # Enqueuing an element
    def enqueue(self, item):
        self.items.append(item)

    # Dequeuing an element
    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()

    # Peeking at the front element of the queue
    def peek(self):
        if not self.is_empty():
            return self.items[0]

    # Checking if the queue is empty
    def is_empty(self):
        return len(self.items) == 0

    # Finding the size of the queue
    def size(self):
        return len(self.items)

    # Copying the queue
    def copy(self):
        new_queue = Queue()
        new_queue.items = self.items.copy()
        return new_queue

    # Merging two queues
    def merge(self, other_queue):
        self.items.extend(other_queue.items)

    # Loop over a queue
    def loop(self):
        for item in self.items:
            print(item)

    # Convert a queue to an array or vice versa
    def to_array(self):
        return list(self.items)

    @classmethod
    def from_array(cls, array):
        queue = cls()
        queue.items = deque(array)
        return queue

    # Sort a queue
    def sort(self):
        self.items = deque(sorted(self.items))

    # Find the maximum or minimum value in a queue
    def max(self):
        if not self.is_empty():
            return max(self.items)

    def min(self):
        if not self.is_empty():
            return min(self.items)

    # Find the sum of all items in a queue
    def sum(self):
        return sum(self.items)

    # Find the average of all items in a queue
    def average(self):
        return sum(self.items) / len(self.items)

    # Find the median of all items in a queue
    def median(self):
        sorted_items = sorted(self.items)
        length = len(sorted_items)
        if length % 2 == 0:
            return (sorted_items[length // 2 - 1] + sorted_items[length // 2]) / 2
        else:
            return sorted_items[length // 2]
