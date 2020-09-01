from data_structures_and_algorithms.challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation

def test_all_brackets():
    all_brackets = '(){}[]'
    expected = True
    actual = multi_bracket_validation(all_brackets)
    assert expected == actual

def test_round_brackets():
    round_brackets = '()'
    expected = True
    actual = multi_bracket_validation(round_brackets)
    assert expected == actual

def test_square_brackets():
    square_brackets = '[]'
    expected = True
    actual = multi_bracket_validation(square_brackets)
    assert expected == actual

def test_curly_brackets():
    curly_brackets = '{}'
    expected = True
    actual = multi_bracket_validation(curly_brackets)
    assert expected == actual

def test_string_inside_brackets():
    string_inside_brackets = '{Hello}(Worled)[!]'
    expected = True
    actual = multi_bracket_validation(string_inside_brackets)
    assert expected == actual

def test_just_open_brackets():
    just_open_brackets = '{(['
    expected = False
    actual = multi_bracket_validation(just_open_brackets)
    assert expected == actual

def test_just_closed_brackets():
    just_closed_brackets = '}])'
    expected = False
    actual = multi_bracket_validation(just_closed_brackets)
    assert expected == actual

def test_open_close_randomly_brackets():
    open_close_randomly_brackets = '(}{][)'
    expected = False
    actual = multi_bracket_validation(open_close_randomly_brackets)
    assert expected == actual  