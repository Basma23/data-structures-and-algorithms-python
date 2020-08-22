from data_structures_and_algorithms.challenges.linked_list.linked_list import Node, LinkedList
import pytest

@pytest.fixture
def prepare_info():
    books = LinkedList()
    a = books.append_info("History")
    b = books.append_info("Kids")
    c = books.append_info("Horror")
    d = books.includes("Novel")
    e = books.insert_between("Novel","Two_City")
    return {"a":a,"b":b,"c":c,"d":d,"e":e,"books":books}

def first_test():
    books = LinkedList()
    books.append_info("History")
    books.append_info("Horror")
    books.includes("Novel")
    expected = 'History -> Horror -> Novel -> None'
    actual = books.__str__()
    assert expected == actual

def second_test(prepare_info):
    prepare_info['books']
    prepare_info['a']
    prepare_info['b']
    prepare_info['c']
    expected = True
    actual = prepare_info['books'].includes("Novel")
    assert expected == actual

def third_test(prepare_info):
    prepare_info['books']
    prepare_info['a']
    prepare_info['b']
    prepare_info['c']
    expected = False
    actual = prepare_info['books'].includes("since")
    assert expected == actual

def fourth_test(prepare_info):
    prepare_info['books']
    prepare_info['a']
    prepare_info['b']
    prepare_info['c']
    expected = 'This function doesn\'t have been initialized yet'
    actual = prepare_info['books'].insert_between("Novel")
    assert expected == actual

def fifth_test(prepare_info):
    new_book = prepare_info['books'].insert('Advanture')
    expected = 'Advanture -> History -> Horror -> Novel -> None'
    actual = prepare_info['books'].__str__()
    assert expected == actual