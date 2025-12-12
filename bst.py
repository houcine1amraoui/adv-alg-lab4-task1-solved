class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        # Create the BST shown in bst.png
        self.root = Node(7)
        self.root.left = Node(4)
        self.root.right = Node(9)
        self.root.left.left = Node(2)
        self.root.left.right = Node(5)
        self.root.right.left = Node(8)
        self.root.right.right = Node(12)
        self.root.left.left.left = Node(0)
        self.root.right.right.right = Node(16)

    def is_valid(self):
        def _is_valid(node, min_val, max_val):
            if node is None:
                return True

            # The current node must be strictly between (min_val, max_val)
            if not (min_val < node.value < max_val):
                return False

            # Left subtree must be < node.value
            # Right subtree must be > node.value
            return (_is_valid(node.left, min_val, node.value) and
                    _is_valid(node.right, node.value, max_val))

        # Start with infinite bounds
        return _is_valid(self.root, float("-inf"), float("inf"))


    def search_iterative(self, value):
        current = self.root
        while current:
            if current.value == value:
                return True
            if value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def search_recursive(self, value):
        def _search(node, value):
            if node is None:
                return False
            if node.value == value:
                return True
            if value < node.value:
                return _search(node.left, value)
            else:
                return _search(node.right, value)

        return _search(self.root, value)
    
    def level_order(self):
        if self.root is None:
            return []
        queue = [self.root]
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def pre_order(self):
        result = []
        def _pre(node):
            if not node:
                return
            result.append(node.value)
            _pre(node.left)
            _pre(node.right)
        _pre(self.root)
        return result

    def in_order(self):
        result = []
        def _in(node):
            if not node:
                return
            _in(node.left)
            result.append(node.value)
            _in(node.right)
        _in(self.root)
        return result

    def post_order(self):
        result = []
        def _post(node):
            if not node:
                return
            _post(node.left)
            _post(node.right)
            result.append(node.value)
        _post(self.root)
        return result
