from data_structures_and_algorithms.data_structures.tree.tree import Node, BinaryTree
from data_structures_and_algorithms.challenges.tree_intersection.tree_intersection import tree_intersection

def test_intersection_tree():
    bt = BinaryTree()
    bt1 = BinaryTree()
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
    actual = tree_intersection(bt, bt1)
    expected = [100, 160, 125, 175, 200, 350, 500]
    assert actual == expected

def test_empty_trees():
    bt = BinaryTree()
    bt1 = BinaryTree()
    actual = tree_intersection(bt, bt1)
    expected = None
    assert actual == expected

def test_unequevelent_trees():
    bt = BinaryTree()
    bt1 = BinaryTree()
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
    bt1.root = Node(42)
    bt1.root.left = Node(100)
    bt1.root.right = Node(600)
    bt1.root.left.left = Node(15)
    bt1.root.left.right = Node(160)
    actual = tree_intersection(bt, bt1)
    expected = [100, 160]
    assert actual == expected

def test_intersection_tree1():
    bt = BinaryTree()
    bt1 = BinaryTree()
    bt.root = Node(0)
    bt.root.left = Node(5)
    bt.root.right = Node(10)
    bt.root.left.left = Node(15)
    bt.root.left.right = Node(20)
    bt1.root = Node(6)
    bt1.root.left = Node(12)
    bt1.root.right = Node(18)
    bt1.root.left.left = Node(24)
    bt1.root.left.right = Node(30)
    actual = tree_intersection(bt, bt1)
    expected = None
    assert actual == expected

def test_intersection_tree2():
    bt = BinaryTree()
    bt1 = BinaryTree()
    bt.root = Node(0)
    bt.root.left = Node(5)
    bt.root.right = Node(10)
    bt.root.left.left = Node(15)
    bt.root.left.right = Node(20)
    bt1.root = Node(5)
    bt1.root.left = Node(15)
    bt1.root.right = Node(10)
    bt1.root.left.left = Node(20)
    bt1.root.left.right = Node(0)
    actual = tree_intersection(bt, bt1)
    expected = [10]
    assert actual == expected