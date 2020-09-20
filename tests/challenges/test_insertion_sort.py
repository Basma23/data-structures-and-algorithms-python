from data_structures_and_algorithms.challenges.insertion_sort.insertion_sort import insertionSort

def test_insertion_sort_empty_array():
    arr_list = []
    actual = insertionSort(arr_list)
    expected = []
    assert actual == expected

def test_insertion_sort():
    arr_list = [8, 4, 23, 42, 16, 15]
    actual = insertionSort(arr_list)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected