from data_structures_and_algorithms.challenges.repeated_word.repeated_word import repeated_word

def test_repeated_word():
    sentence = "Once upon a time, there was a brave princess who..."
    actual = repeated_word(sentence)
    expected = 'a'
    assert actual == expected

def test_unrepeated_word():
    sentence = "Realy nice"
    actual = repeated_word(sentence)
    expected = None
    assert actual == expected