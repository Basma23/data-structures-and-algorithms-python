from data_structures_and_algorithms.challenges.queue_with_stacks.queue_with_stacks import PseudoQueue

def test_unvalid_input_to_pseudo_queue():
    pseudo_queue = PseudoQueue()
    assert pseudo_queue.enqueue(None) == 'Not a valid input'

# def test_empty_pseudo_queue():
#     pseudo_queue = PseudoQueue()
#     assert pseudo_queue.dequeue() == 'Empty'
#     assert pseudo_queue.peek() == 'Empty'

# def test_inserting_to_pseudo_queue():
#     pseudo_queue = PseudoQueue()
#     pseudo_queue.enqueue(2)
#     pseudo_queue.enqueue(4)
#     pseudo_queue.enqueue(6)
#     pseudo_queue.enqueue(8)
#     expected = [8, 6, 4, 2]
#     actual = pseudo_queue.items
#     assert expected == actual

# def test_dequeue_and_peek_in_pseudo_queue():
#     pseudo_queue = PseudoQueue()
#     pseudo_queue.enqueue(2)
#     pseudo_queue.enqueue(4)
#     pseudo_queue.enqueue(6)
#     pseudo_queue.enqueue(8)
#     expected = 2
#     actual = pseudo_queue.dequeue()
#     expected1 = [8, 6, 4]
#     actual1 = pseudo_queue.items
#     assert expected == actual
#     assert expected1 == actual1
    
def test_enqueue():
    queue = PseudoQueue()
    queue.enqueue(5)
    assert queue.__str__() == 'Rear -> {5} -> Front'

def test_dequeue():
    queue = PseudoQueue()
    queue.enqueue(5)
    assert queue.dequeue() == 5