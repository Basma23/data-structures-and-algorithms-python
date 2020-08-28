from data_structures_and_algorithms.challenges.array_shift.array_shift import shift_array

# from data_structures_and_algorithms.challenges.array_shift.array_shift import shift_array

def test_shift_array():
    actual = shift_array([2,4,6,8], 5)
    expected = [2,4,5,6,8]
    assert actual == expected

def test_shift_array_1():
    actual = shift_array([4,8,15,23,42], 16)
    expected = [4,8,15,16,23,42]
    assert actual == expected    

def test_shift_array_2():
    actual = shift_array([0,1,3,23,42], 0)
    expected = [0, 0, 1, 3, 23, 42]
    assert actual == expected  

def test_shift_array_3():
    actual = shift_array([-10,0,1,3,23,42], -5)
    expected = [-10, -5, 0, 1, 3, 23, 42]
    assert actual == expected  