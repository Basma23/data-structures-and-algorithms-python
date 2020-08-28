from data_structures_and_algorithms.challenges.ll_zip.ll_zip import LinkedList, zip_lists
# import pytest

# @pytest.fixture

def test_first_zip_list():
    first_ll = LinkedList([1, False, 3, 5])
    second_ll = LinkedList([7, 'Basma', 9])
    third_ll = zip_lists(first_ll, second_ll)
    actual = '1 -> 7 -> False -> Basma -> 3 -> 9 -> 5 -> None'
    expected = third_ll.__str__()
    assert expected == actual

def test_second_zip_list():
    first_ll = LinkedList([1, False, 3, 5])
    second_ll = LinkedList([7, 'Basma', 9, 11])
    third_ll = zip_lists(first_ll, second_ll)
    actual = '1 -> 7 -> False -> Basma -> 3 -> 9 -> 5 -> 11 -> None'
    expected = third_ll.__str__()
    assert expected == actual

def test_third_zip_list():
    first_ll = LinkedList([1, False, 3])
    second_ll = LinkedList([7, 'Basma', 9, 11])
    third_ll = zip_lists(first_ll, second_ll)
    actual = '1 -> 7 -> False -> Basma -> 3 -> 9 -> 11 -> None'
    expected = third_ll.__str__()
    assert expected == actual