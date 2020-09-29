from data_structures_and_algorithms.data_structures.tree.tree import Node, BinaryTree

def tree_intersection(bt1, bt2):
    result = [] 
    if not bt1.root or not bt2.root:
        return None
    def _walk(root1, root2):
        if root1 and root2:
            if root1.value == root2.value:
                result.append(root1.value)
            _walk(root1.left, root2.left)
            _walk(root1.right, root2.right)
    _walk(bt1.root, bt2.root)
    if result:
        return result
    return None

if __name__ == '__main__':
    bt = BinaryTree()
    bt.root = Node(150)
    bt.root.left = Node(100)
    bt.root.right = Node(250)
    bt.root.left.left = Node(75)
    bt.root.left.right = Node(160)
    bt.root.right.left = Node(200)
    bt.root.right.right = Node(350)
    bt.root.left.right.left = Node(125)
    bt.root.left.right.right = Node(175)
    bt.root.right.right.left = Node(300)
    bt.root.right.right.right = Node(500)
    print(bt.pre_order()) 
    bt1 = BinaryTree()
    bt1.root = Node(42)
    bt1.root.left = Node(100)
    bt1.root.right = Node(600)
    bt1.root.left.left = Node(15)
    bt1.root.left.right = Node(160)
    bt1.root.right.left = Node(200)
    bt1.root.right.right = Node(350)
    bt1.root.left.right.left = Node(125)
    bt1.root.left.right.right = Node(175)
    bt1.root.right.right.left = Node(4)
    bt1.root.right.right.right = Node(500)  
    print(bt1.pre_order()) 
    print(tree_intersection(bt, bt1))