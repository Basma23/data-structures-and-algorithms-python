from data_structures_and_algorithms.challenges.ll_zip.ll_zip import LinkedList
# import pytest

# @pytest.fixture

def test_first_zip_list():
    first = LinkedList()
    second = LinkedList()
    first.append(2)
    first.append(4)
    first.append(6)
    second.append(5)
    second.append(7)
    second.append(9)
    first.zip_lists(second)
    actual = first.display()
    expected = [2, 5, 4, 7, 6, 9]
    assert expected ==actual

def test_second_zip_list():
    first = LinkedList()
    second = LinkedList()
    first.zip_lists(second)
    actual = first.display()
    expected = []
    assert expected == actual