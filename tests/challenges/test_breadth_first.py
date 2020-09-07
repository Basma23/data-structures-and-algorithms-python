from data_structures_and_algorithms.challenges.breadth_first.breadth_first import Node, BinaryTree, breadth_first_traversal

def test_empty_tree():
    bt = BinaryTree()
    assert breadth_first_traversal(bt.root) == 'The tree is empty'

def test_breadth_first():
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
    expected = [2, 7, 5, 2, 6, 9, 5, 11, 4]
    actual = breadth_first_traversal(bt.root)
    assert expected == actual