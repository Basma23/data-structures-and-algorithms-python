from data_structures_and_algorithms.challenges.quick_sort.quick_sort import *

def test_quick_sort_empty_array():
    arr = []
    n = len(arr)
    expected = []
    actual = quick_sort(arr, 0, n - 1)
    assert actual == expected

def test_quick_sort_array():
    arr = [50, 10, 5, 20, 15, 30, 45, 40, 35, 25]
    n = len(arr)
    expected = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    actual = quick_sort(arr, 0, n - 1)
    assert actual == expected