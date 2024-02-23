class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    # Inserting a node
    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if not node.left:
                node.left = Node(data)
            else:
                self._insert(node.left, data)
        else:
            if not node.right:
                node.right = Node(data)
            else:
                self._insert(node.right, data)

    # Removing a node
    def remove(self, data):
        self.root = self._remove(self.root, data)

    def _remove(self, node, data):
        if not node:
            return node
        if data < node.data:
            node.left = self._remove(node.left, data)
        elif data > node.data:
            node.right = self._remove(node.right, data)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                temp = self._min_value_node(node.right)
                node.data = temp.data
                node.right = self._remove(node.right, temp.data)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Searching for a node
    def search(self, data):
        return self._search(self.root, data)

    def _search(self, node, data):
        if not node:
            return False
        if node.data == data:
            return True
        if data < node.data:
            return self._search(node.left, data)
        else:
            return self._search(node.right, data)

    # Traversing the tree (pre-order, in-order, post-order, level-order)
    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, node):
        if node:
            print(node.data)
            self._preorder(node.left)
            self._preorder(node.right)

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.data)
            self._inorder(node.right)

    def postorder(self):
        self._postorder(self.root)

    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.data)

    def levelorder(self):
        if not self.root:
            return
        queue = []
        queue.append(self.root)
        while queue:
            node = queue.pop(0)
            print(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    # Finding the height of the tree
    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if not node:
            return -1
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        return max(left_height, right_height) + 1

    # Finding the depth of a node
    def depth(self, data):
        return self._depth(self.root, data, 0)

    def _depth(self, node, data, current_depth):
        if not node:
            return -1
        if node.data == data:
            return current_depth
        left_depth = self._depth(node.left, data, current_depth + 1)
        right_depth = self._depth(node.right, data, current_depth + 1)
        if left_depth != -1:
            return left_depth
        else:
            return right_depth

    # Finding the size of the tree
    def size(self):
        return self._size(self.root)

    def _size(self, node):
        if not node:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)

    # Finding the number of leaves
    def num_leaves(self):
        return self._num_leaves(self.root)

    def _num_leaves(self, node):
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        return self._num_leaves(node.left) + self._num_leaves(node.right)

    # Finding the number of internal nodes
    def num_internal_nodes(self):
        return self.size() - self.num_leaves()

    # Finding the lowest common ancestor of two nodes
    def lowest_common_ancestor(self, node1, node2):
        return self._lowest_common_ancestor(self.root, node1, node2)

    def _lowest_common_ancestor(self, node, node1, node2):
        if not node:
            return None
        if node.data == node1 or node.data == node2:
            return node
        left_ancestor = self._lowest_common_ancestor(node.left, node1, node2)
        right_ancestor = self._lowest_common_ancestor(node.right, node1, node2)
        if left_ancestor and right_ancestor:
            return node
        return left_ancestor if left_ancestor else right_ancestor

    # Checking if the tree is balanced
    def is_balanced(self):
        return self._is_balanced(self.root) != -1

    def _is_balanced(self, node):
        if not node:
            return 0
        left_height = self._is_balanced(node.left)
        right_height = self._is_balanced(node.right)
        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1
