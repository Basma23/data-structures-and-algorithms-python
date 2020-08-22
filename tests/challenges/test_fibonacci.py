from data_structures_and_algorithms.challenges.fibonacci.fibonacci import fibonacci, fibonacci_in_loop

def test_of_fibonacci():
    expected = 34
    actual = fibonacci(9)
    assert actual == expected

def test_fib_zero():
    expected = 0
    actual = fibonacci(0)
    assert actual == expected

def test_fib_one():
    expected = 1
    actual = fibonacci(1)
    assert actual == expected

def test_fib_neg():
    expected = 0
    actual = fibonacci(-10)
    assert actual == expected

def test_of_fibonacci_in_loop():
    expected = 34
    actual = fibonacci_in_loop(9)
    assert actual == expected

def test_fib_zero_in_loop():
    expected = 0
    actual = fibonacci_in_loop(0)
    assert actual == expected

def test_fib_one_in_loop():
    expected = 1
    actual = fibonacci_in_loop(1)
    assert actual == expected

# def test_fib_neg_in_loop():
#     expected = 0
#     actual = fibonacci_in_loop(-10)
#     assert actual == expected