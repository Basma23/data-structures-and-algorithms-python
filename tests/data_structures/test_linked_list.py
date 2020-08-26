from data_structures_and_algorithms.data_structures.linked_list.linked_list import (
    LinkedList, Node
)
import pytest


# def test_instance():
#     ll = LinkedList()
#     assert isinstance(ll, LinkedList)

@pytest.fixture
def first_test():
    drinks = LinkedList()
    drinks.append("Coffee")
    drinks.append("Ice_Tea")
    drinks.includes("Lemonade")
    expected = 'Coffee -> Ice_Tea -> Lemonade -> None'
    actual = drinks.__str__()
    assert expected == actual

# def second_test(prepare_info):
#     prepare_info['drinks']
#     prepare_info['a']
#     prepare_info['b']
#     prepare_info['c']
#     expected = True
#     actual = prepare_info['drinks'].includes("Lemonade")
#     assert expected == actual

def third_test(prepare_info):
    prepare_info['drinks']
    prepare_info['a']
    prepare_info['b']
    prepare_info['c']
    expected = False
    actual = prepare_info['drinks'].includes("Milk")
    assert expected == actual

def fourth_test(prepare_info):
    new_drink = prepare_info['drinks'].insert('Milk')
    expected = 'Milk -> Coffee -> Ice_Tea -> Lemonade -> None'
    actual = prepare_info['drinks'].__str__()
    assert expected == actual

def fifth_test():
    drinks = LinkedList()
    drinks.append('Coffee')
    drinks.append('Ice_Tea')
    drinks.append('Lemonade')
    drinks.append('Mocha')
    drinks.insertBefore('Mocha', 'milkcheck')
    expected = 'Coffee -> Ice_Tea -> Lemonade -> milkcheck -> Mocha -> None'
    actual = drinks.__str__()
    assert expected == actual

def sixth_test():
    drinks = LinkedList()
    drinks.append('Coffee')
    drinks.append('Ice_Tea')
    drinks.append('Lemonade')
    drinks.append('Mocha')
    drinks.insertBefore('Mocha', 'milkcheck')
    drinks.insertAfter(drinks.head.next, 'Milk')
    drinks.deleteNode('Mocha')
    expected = 'Coffee -> Ice_Tea -> Milk -> Lemonade -> milkcheck -> None'
    actual = drinks.__str__()
    assert expected == actual

def seventh_test():
    drinks = LinkedList()
    drinks.append('Coffee')
    drinks.append('Ice_Tea')
    drinks.append('Lemonade')
    drinks.append('Mocha')
    drinks.insertBefore('Mocha', 'milkcheck')
    drinks.insertAfter(drinks.head.next, 'Milk')
    drinks.deleteNode('Mocha')
    drinks.get_kth_from_end_ll(4)
    expected = 'Ice_Tea'
    actual = drinks.__str__()
    assert expected == actual

def eight_test():
    drinks = LinkedList()
    drinks.append('Coffee')
    drinks.append('Ice_Tea')
    drinks.append('Lemonade')
    drinks.append('Mocha')
    drinks.insertBefore('Mocha', 'milkcheck')
    drinks.insertAfter(drinks.head.next, 'Milk')
    drinks.deleteNode('Mocha')
    drinks.get_kth_from_end_ll(6)
    expected = 'Location is greater than the length of LinkedList'
    actual = drinks.__str__()
    assert expected == actual

def ninht_test():
    drinks = LinkedList()
    drinks.append('Coffee')
    drinks.append('Ice_Tea')
    drinks.append('Lemonade')
    drinks.append('Mocha')
    drinks.insertBefore('Mocha', 'milkcheck')
    drinks.insertAfter(drinks.head.next, 'Milk')
    drinks.deleteNode('Mocha')
    drinks.get_kth_from_end_ll(5)
    expected = 'Coffee'
    actual = drinks.__str__()
    assert expected == actual