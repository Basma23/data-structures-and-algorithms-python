from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues import Node, Stack, Queue

def test_one_stack():
    fruites = Stack()
    fruites.push('Orange')
    fruites.push('Pineapple')
    fruites.push('Berry')
    expected = ['Orange', 'Pineapple', 'Berry']
    actual = fruites.items
    assert expected == actual

def test_two_stack():
    fruites = Stack()
    fruites.push('Orange')
    fruites.push('Pineapple')
    fruites.push('Berry')
    expected = 'Berry'
    actual = fruites.peek()
    assert expected == actual

def test_three_stack():
    fruites = Stack()
    fruites.push('Orange')
    fruites.push('Pineapple')
    fruites.push('Berry')
    expected = 'Berry'
    actual = fruites.pop()
    assert expected == actual

def test_one_queue():
    fruit = Queue()
    fruit.enqueue('Mango')
    fruit.enqueue('Strawberry')
    fruit.enqueue('Peach')
    expected = ['Mango', 'Strawberry', 'Peach']
    actual = fruit.items
    assert expected == actual

def test_two_queue():
    fruit = Queue()
    fruit.enqueue('Mango')
    fruit.enqueue('Strawberry')
    fruit.enqueue('Peach')
    expected = 'Mango'
    actual = fruit.front.info
    assert expected == actual

def test_three_queue():
    fruit = Queue()
    fruit.enqueue('Mango')
    fruit.enqueue('Strawberry')
    fruit.enqueue('Peach')
    expected = 'Peach'
    actual = fruit.rear.info
    assert expected == actual

def test_four_queue():
    fruit = Queue()
    fruit.enqueue('Mango')
    fruit.enqueue('Strawberry')
    fruit.enqueue('Peach')
    expected = 'Mango'
    actual = fruit.peek()
    assert expected == actual

def test_five_queue():
    fruit = Queue()
    fruit.enqueue('Mango')
    fruit.enqueue('Strawberry')
    fruit.enqueue('Peach')
    expected = 'Mango'
    actual = fruit.dequeue()
    assert expected == actual