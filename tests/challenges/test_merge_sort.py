from data_structures_and_algorithms.challenges.merge_sort.merge_sort import mergeSort

def test_merge_sort_empty_array():
    arr_list = []
    actual = mergeSort(arr_list)
    expected = []
    assert actual == expected

def test_merge_sort_array():
    arr_list = [12, 11, 13, 5, 6, 7]
    actual = mergeSort(arr_list)
    expected = [5, 6, 7, 11, 12, 13]
    assert actual == expected
