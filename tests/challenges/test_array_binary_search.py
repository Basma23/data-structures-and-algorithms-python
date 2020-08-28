from data_structures_and_algorithms.challenges.array_binary_search.array_binary_search import BinarySearch

def test_binary_one():
    expected = -1
    actual = BinarySearch([11,22,33,44,55,66,77], 90)
    assert expected == actual

def test_binary_two():
    expected = 5
    actual = BinarySearch([4,8,15,16,23,42], 42)
    assert expected == actual