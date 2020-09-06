from data_structures_and_algorithms.challenges.find_maximum_value.find_maximum_value import Node, find_maximum_value

def test_find_maximum_value_one():
    root = Node(7)
    root.left = Node(13)
    root.right = Node(5)
    root.left.left = Node(8)
    root.left.right = Node(9)
    root.right.left = Node(100)
    root.right.right = Node(-4)
    actual = find_maximum_value(root)
    expected = 100
    assert actual == expected

def test_find_maximum_value_for_negative():
    root = Node(-7)
    root.left = Node(-13)
    root.right = Node(-5)
    root.left.left = Node(-8)
    root.left.right = Node(-9)
    root.right.left = Node(-100)
    root.right.right = Node(-4)
    actual = find_maximum_value(root)
    expected = -4
    assert actual == expected

    
def test_find_maximum_value_if_we_have_left_right_only():
    root = Node(7)
    root.left = Node(13)
    root.right = Node(5)
    actual = find_maximum_value(root)
    expected = 13
    assert actual == expected

def test_find_maximum_value_if_we_have_only_one_node():
    root = Node(7)
    actual = find_maximum_value(root)
    expected = 7
    assert actual == expected