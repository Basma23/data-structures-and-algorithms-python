class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        output = []
        def _walk(node):
            if not node:
                return
            output.append(node.value)
            _walk(node.left)
            _walk(node.right)

        _walk(self.root)
        return output

    def in_order(self):
        output = []
        def _walk(node):
            if not node:
                return
            _walk(node.left) 
            output.append(node.value)
            _walk(node.right)

        _walk(self.root)
        return output

    def post_order(self):
        output = []
        def _walk(node):
            if not node:
                return
            _walk(node.left) 
            _walk(node.right)
            output.append(node.value)

        _walk(self.root)
        return output

class BinarySearchTree(BinaryTree):
    def add(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            current = self.root
            while (current):
                if current.value > value: 
                    if current.left == None: 
                        current.left = Node(value)
                        break
                    current = current.left
                else:
                    if current.right == None: 
                        current.right = Node(value)
                        break
                    current = current.right  

    def contains(self, value): 
        try:
            if not self.root:
                return 'value not found'
            else:
                current = self.root
                while (current):
                    if current.value==value:
                        return True
                    if current.value > value: 
                        if current.left == None: 
                            return 'value not found'
                        current = current.left
                    else:
                        if current.right == None: 
                            return 'value not found'
                        current = current.right
        except:
            print("something wrong happened try again") 

if __name__ == '__main__':
    bt = BinaryTree()
    bt.root = Node(7)
    bt.root.left = Node(13)
    bt.root.right = Node(5)
    bt.root.left.left = Node(8)
    bt.root.left.right = Node(9)
    bt.root.right.left = Node(1)
    bt.root.right.right = Node(-4)
    print(bt.pre_order()) 
    print(bt.in_order()) 
    print(bt.post_order()) 
    