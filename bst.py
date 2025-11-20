class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        # create the bst shown in bst.png
        self.root = Node(7)
        self.root.left = Node(4)
        self.root.right = Node(9)
        self.root.left.left = Node(2)
        self.root.left.right = Node(5)
        self.root.right.left = Node(8)
        self.root.right.right = Node(12)
        self.root.left.left.left = Node(0)
        self.root.right.right.right = Node(16)

    def search_iterative(self, value):
        current = self.root
        while current:
            # complete code here
            if current.value == value:
                return True
            if value < current.value:
                current = current.left  
            else: 
                current = current.right
        return False
    
    def search_recrusive(self, value):
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
        # put your code here
        if self.root == None:
            return
        q = [] # my_queue = Queue()
        print(self.root.value, end=" -> ")
        q.append(self.root)
        while q != []:
            p = q.pop(0)
            if p.left:
                print(p.left.value, end=" ->")
                q.append(p.left)

            if p.right:
                print(p.right.value, end=" ->")
                q.append(p.right)

    def pre_order(self):
        # put your code here
        def _pre_order(node):
            if node:
                print(node.value)
                _pre_order(node.left)
                _pre_order(node.right)
        return _pre_order(self.root)

    def in_order(self):
        # put your code here
        def _in_order(node):
            if node:
                _in_order(node.left)
                print(node.value)
                _in_order(node.right)
        return _in_order(self.root)

    def post_order(self):
        # put your code here
        def _post_order(node):
            if node:
                _post_order(node.left)
                _post_order(node.right)
                print(node.value)
        return _post_order(self.root)