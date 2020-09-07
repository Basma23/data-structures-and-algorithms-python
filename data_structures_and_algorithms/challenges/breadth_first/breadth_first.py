from data_structures_and_algorithms.data_structures.tree.tree import Node, BinaryTree

def breadth_first_traversal(root): 
    breadth = []
    output = []
    if not root:
        return 'The tree is empty'
    else:
        if root:
            output.append(root)
        while output:
            current = output.pop(0)
            breadth.append(current.value)
            if current.left:
                output.append(current.left)
            if current.right:
                output.append(current.right)
    return breadth

if __name__ == '__main__':
    bt = BinaryTree()
    bt.root = Node(2) 
    bt.root.left = Node(7) 
    bt.root.right = Node(5) 
    bt.root.left.left = Node(2) 
    bt.root.left.right = Node(6)
    bt.root.left.right.left = Node(5)
    bt.root.left.right.right = Node(11)
    bt.root.right.right = Node(9)
    bt.root.right.right.left = Node(4)
    print(breadth_first_traversal(bt.root))