import heapq

class Heap:
    def __init__(self):
        self.items = []

    # Inserting an element into the heap
    def insert(self, item):
        heapq.heappush(self.items, item)

    # Removing the top element from the heap
    def remove_top(self):
        if not self.is_empty():
            return heapq.heappop(self.items)

    # Peeking at the top element of the heap
    def peek(self):
        if not self.is_empty():
            return self.items[0]

    # Checking if the heap is empty
    def is_empty(self):
        return len(self.items) == 0

    # Finding the size of the heap
    def size(self):
        return len(self.items)

    # Copying the heap
    def copy(self):
        new_heap = Heap()
        new_heap.items = self.items.copy()
        return new_heap

    # Merging two heaps
    def merge(self, other_heap):
        self.items.extend(other_heap.items)
        heapq.heapify(self.items)

    # Convert a heap to an array or vice versa
    def to_array(self):
        return list(self.items)

    @classmethod
    def from_array(cls, array):
        heap = cls()
        heap.items = array.copy()
        heapq.heapify(heap.items)
        return heap

    # Sort a heap
    def sort(self):
        sorted_items = []
        while self.items:
            sorted_items.append(heapq.heappop(self.items))
        return sorted_items

    # Find the maximum or minimum item in a range
    def max(self, start, end):
        return max(self.items[start:end])

    def min(self, start, end):
        return min(self.items[start:end])

    # Find the median of all items in a heap
    def median(self):
        sorted_items = self.sort()
        length = len(sorted_items)
        if length % 2 == 0:
            return (sorted_items[length // 2 - 1] + sorted_items[length // 2]) / 2
        else:
            return sorted_items[length // 2]

    # Update an item in the heap
    def update(self, old_item, new_item):
        index = self.items.index(old_item)
        self.items[index] = new_item
        heapq.heapify(self.items)

    # Get the parent or child of an item in the heap
    def parent(self, index):
        return self.items[(index - 1) // 2]

    def left_child(self, index):
        return self.items[2 * index + 1]

    def right_child(self, index):
        return self.items[2 * index + 2]

    # Get the height or depth of the heap
    def height(self):
        return (len(self.items) - 1).bit_length()

    def depth(self, index):
        return (index + 1).bit_length() - 1

    # Clear a heap
    def clear(self):
        self.items.clear()
