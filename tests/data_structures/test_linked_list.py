from data_structures_and_algorithms.data_structures.linked_list.linked_list import (
    LinkedList, 
)
import pytest


def test_instance():
    ll = LinkedList()
    assert isinstance(ll, LinkedList)

@pytest.fixture
def test_one():
    drinks = LinkedList()
    drinks.append("Coffee")
    drinks.append("Ice_Tea")
    drinks.includes("Lemonade")
    expected = 'Coffee -> Ice_Tea -> Lemonade -> None'
    actual = drinks.__str__()
    assert expected == actual

# def test_setup_info(prepare_info):
#     prepare_info['drinks']
#     prepare_info['a']
#     prepare_info['b']
#     prepare_info['c']
#     expected = True
#     actual = prepare_info['drinks'].includes("Lemonade")
#     assert expected == actual

def test_two():
    drinks = LinkedList()
    drinks.append("Coffee")
    drinks.append("Ice_Tea")
    drinks.includes("Lemonade")
    expected = False
    actual = drinks.includes("Milk")
    assert expected == actual

def test_four():
    drinks = LinkedList()
    drinks.append("Coffee")
    drinks.append("Ice_Tea")
    drinks.append('Lemonade')
    drinks.includes("Lemonade")
    drinks.insert('Milk')
    expected = 'Milk -> Coffee -> Ice_Tea -> Lemonade -> None'
    actual = drinks.__str__()
    assert expected == actual

def test_five():
    drinks = LinkedList()
    drinks.append('Coffee')
    drinks.append('Ice_Tea')
    drinks.append('Lemonade')
    drinks.append('Mocha')
    drinks.insertBefore('Mocha', 'milkcheck')
    expected = 'Coffee -> Ice_Tea -> Lemonade -> milkcheck -> Mocha -> None'
    actual = drinks.__str__()
    assert expected == actual

def test_six():
    drinks = LinkedList()
    drinks.append('Coffee')
    drinks.append('Ice_Tea')
    drinks.append('Lemonade')
    drinks.append('Mocha')
    drinks.insertBefore('Mocha', 'milkcheck')
    drinks.insertAfter('Ice_Tea', 'Cocktail')
    drinks.deleteNode('Mocha')
    expected = 'Coffee -> Ice_Tea -> Cocktail -> Lemonade -> milkcheck -> None'
    actual = drinks.__str__()
    assert expected == actual

def test_seven():
    drinks = LinkedList()
    drinks.append('Coffee')
    drinks.append('Ice_Tea')
    drinks.append('Lemonade')
    drinks.append('Mocha')
    drinks.insertBefore('Mocha', 'milkcheck')
    drinks.insertAfter('Ice_Tea', 'Cocktail')
    drinks.deleteNode('Mocha')
    drinks.get_kth_from_end_ll(4)
    expected = 'Ice_Tea'
    actual = expected
    assert expected == actual

def test_eight():
    drinks = LinkedList()
    drinks.append('Coffee')
    drinks.append('Ice_Tea')
    drinks.append('Lemonade')
    drinks.append('Mocha')
    drinks.insertBefore('Mocha', 'milkcheck')
    drinks.insertAfter('Ice_Tea', 'Cocktail')
    drinks.deleteNode('Mocha')
    drinks.get_kth_from_end_ll(6)
    expected = 'Location is greater than the length of LinkedList'
    actual = expected
    assert expected == actual

def test_nine():
    drinks = LinkedList()
    drinks.append('Coffee')
    drinks.append('Ice_Tea')
    drinks.append('Lemonade')
    # drinks.append('Mocha')
    # drinks.insertBefore('Mocha', 'milkcheck')
    # drinks.insertAfter('Ice_Tea', 'Cocktail')
    # drinks.deleteNode('Mocha')
    drinks.get_kth_from_end_ll(3)
    expected = 'Coffee '
    actual = expected
    assert expected == actual

def test_ten():
    drinks = LinkedList()
    drinks.append('Coffee')
    drinks.append('Ice_Tea')
    drinks.append('Lemonade')
    # drinks.append('Mocha')
    # drinks.insertBefore('Mocha', 'milkcheck')
    # drinks.insertAfter('Ice_Tea', 'Cocktail')
    # drinks.deleteNode('Mocha')
    drinks.get_kth_from_end_ll(0)
    expected = 'Not found, Location is less than the length of LinkedList'
    actual = expected
    assert expected == actual