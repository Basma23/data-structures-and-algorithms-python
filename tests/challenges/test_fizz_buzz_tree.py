from data_structures_and_algorithms.challenges.fizz_buzz_tree.fizz_buzz_tree import fizz_buzz, fizz_buzz_tree, BinaryTree, Node
import pytest

@pytest.fixture
def my_tree():
    bt = BinaryTree()
    bt.root = Node(3)
    bt.root.left = Node(5)
    bt.root.right = Node(6)
    bt.root.left.left = Node(10)
    bt.root.left.right = Node(9)
    bt.root.right.right = Node(15)
    bt.root.left.left.left = Node(2)
    bt.root.right.right.left = Node(4)
    return bt

def test_fizz_buzz3(my_tree):
    tree_test = my_tree
    new_tree = fizz_buzz_tree(tree_test)
    assert new_tree.root.value == "Fizz"

def test_fizz_buzz5(my_tree):
    tree_test = my_tree
    new_tree = fizz_buzz_tree(tree_test)
    assert new_tree.root.left.value == "Buzz"

def test_fizz_buzz6(my_tree):
    tree_test = my_tree
    new_tree = fizz_buzz_tree(tree_test)
    assert new_tree.root.right.value == "Fizz"

def test_fizz_buzz10(my_tree):
    tree_test = my_tree
    new_tree = fizz_buzz_tree(tree_test)
    assert new_tree.root.left.left.value == "Buzz"

def test_fizz_buzz9(my_tree):
    tree_test = my_tree
    new_tree = fizz_buzz_tree(tree_test)
    assert new_tree.root.left.right.value == "Fizz"


def test_fizz_buzz15(my_tree):
    tree_test = my_tree
    new_tree = fizz_buzz_tree(tree_test)
    assert new_tree.root.right.right.value == "FizzBuzz"

def test_fizz_buzz2_samevalue(my_tree):
    tree_test = my_tree
    new_tree = fizz_buzz_tree(tree_test)
    assert new_tree.root.left.left.left.value == "2"

def test_fizz_buzz4_samevalue(my_tree):
    tree_test = my_tree
    new_tree = fizz_buzz_tree(tree_test)
    assert new_tree.root.right.right.left.value == "4"

def test_empty_tree():
    tree = BinaryTree()
    new_tree = fizz_buzz_tree(tree)
    assert new_tree.root == None