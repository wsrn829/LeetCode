class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Inserting a node at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Inserting a node at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Inserting a node at a specific position
    def insert_at_position(self, position, data):
        if position == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current_node = self.head
        for _ in range(position - 1):
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node

    # Removing the first node
    def remove_first_node(self):
        if self.head:
            self.head = self.head.next

    # Removing the last node
    def remove_last_node(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

    # Removing a node at a specific position
    def remove_node_at_position(self, position):
        if position == 0:
            self.remove_first_node()
            return
        current_node = self.head
        for _ in range(position - 1):
            current_node = current_node.next
        current_node.next = current_node.next.next

    # Finding the length of the linked list
    def length(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    # Reversing the linked list
    def reverse(self):
        prev = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next_node
        self.head = prev

    # Copying the linked list
    def copy(self):
        new_linked_list = LinkedList()
        current_node = self.head
        while current_node:
            new_linked_list.insert_at_end(current_node.data)
            current_node = current_node.next
        return new_linked_list

    # Merging two linked lists
    def merge(self, other_linked_list):
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = other_linked_list.head

    # Loop over linked list
    def loop(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    # Find a node
    def find(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return current_node
            current_node = current_node.next
        return None

    # Insert a node
    def insert(self, position, data):
        if position == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current_node = self.head
        for _ in range(position - 1):
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node

    # Remove a node
    def remove(self, data):
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return
        prev = None
        while current_node and current_node.data != data:
            prev = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev.next = current_node.next
        current_node = None

    # Update a node
    def update(self, position, data):
        current_node = self.head
        for _ in range(position):
            current_node = current_node.next
        current_node.data = data

    # Swap two nodes
    def swap_nodes(self, position1, position2):
        current_node1 = self.head
        for _ in range(position1):
            current_node1 = current_node1.next
        current_node2 = self.head
        for _ in range(position2):
            current_node2 = current_node2.next
        current_node1.data, current_node2.data = current_node2.data, current_node1.data

    # Get the first or last node in the list
    def get_first_node(self):
        return self.head

    def get_last_node(self):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        return current_node

    # Get the length of the list
    def get_length(self):
        return self.length()

    # Check if a node exists in the list
    def node_exists(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    # Convert a linked list to an array or vice versa
    def to_array(self):
        array = []
        current_node = self.head
        while current_node:
            array.append(current_node.data)
            current_node = current_node.next
        return array

    @classmethod
    def from_array(cls, array):
        linked_list = cls()
        for item in array:
            linked_list.insert_at_end(item)
        return linked_list

    # Clone a linked list
    def clone(self):
        return self.copy()

    # Sort a linked list
    def sort(self):
        array = self.to_array()
        array.sort()
        return LinkedList.from_array(array)

    # Detect a loop in a linked list
    def has_loop(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    # Remove duplicates from a linked list
    def remove_duplicates(self):
        current_node = self.head
        while current_node:
            next_node = current_node.next
            while next_node:
                if current_node.data == next_node.data:
                    current_node.next = next_node.next
                    next_node = None
                else:
                    next_node = next_node.next
            current_node = current_node.next

    # Find the middle node of a linked list
    def middle_node(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data
