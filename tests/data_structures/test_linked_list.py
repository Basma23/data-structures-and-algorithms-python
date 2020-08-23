from data_structures_and_algorithms.data_structures.linked_list.linked_list import (
    LinkedList,
)
import pytest


def test_instance():
    ll = LinkedList()
    assert isinstance(ll, LinkedList)

@pytest.fixture
def prepare_info():
    drinks = LinkedList()
    a = drinks.append("Coffee")
    b = drinks.append("Ice_Tea")
    c = drinks.append("Lemonade")
    d = drinks.includes("Mocha")
    return {"a":a,"b":b,"c":c,"d":d,"e":e,"drinks":drinks}

def first_test():
    drinks = LinkedList()
    drinks.append("Coffee")
    drinks.append("Ice_Tea")
    drinks.includes("Lemonade")
    expected = 'Coffee -> Ice_Tea -> Lemonade -> None'
    actual = drinks.__str__()
    assert expected == actual

def second_test(prepare_info):
    prepare_info['drinks']
    prepare_info['a']
    prepare_info['b']
    prepare_info['c']
    expected = True
    actual = prepare_info['drinks'].includes("Lemonade")
    assert expected == actual

def third_test(prepare_info):
    prepare_info['drinks']
    prepare_info['a']
    prepare_info['b']
    prepare_info['c']
    expected = False
    actual = prepare_info['drinks'].includes("Milk")
    assert expected == actual

def fourth_test(prepare_info):
    new_book = prepare_info['drinks'].insert('Milk')
    expected = 'Milk -> History -> Horror -> Novel -> None'
    actual = prepare_info['drinks'].__str__()
    assert expected == actual
