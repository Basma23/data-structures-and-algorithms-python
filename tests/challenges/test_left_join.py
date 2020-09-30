from data_structures_and_algorithms.challenges.left_join.left_join import left_join

def test_empty_decs():
    ht = {}
    ht1 = {}
    actual = left_join(ht, ht1)
    expected = []
    assert actual == expected

def test_lift_join_empty_dec():
    ht = {'fond':'enamored','wrath':'anger','diligent':'employed','outift':'garb','guide':'usher'}
    ht1 = {}
    actual = left_join(ht, ht1)
    expected = [
        ['fond', 'enamored', 'NULL'], 
        ['wrath', 'anger', 'NULL'], 
        ['diligent', 'employed', 'NULL'], 
        ['outift', 'garb', 'NULL'], 
        ['guide', 'usher', 'NULL']
    ]
    assert actual == expected

def test_lift_join():
    ht = {'fond':'enamored','wrath':'anger','diligent':'employed','outift':'garb','guide':'usher'}
    ht1 = {'fond':'averse','wrath':'delight','diligent':'idle','guide':'follow','flow':'jam'}
    actual = left_join(ht, ht1)
    expected = [
        ['fond', 'enamored', 'averse'], 
        ['wrath', 'anger', 'delight'], 
        ['diligent', 'employed', 'idle'], 
        ['outift', 'garb', 'NULL'], 
        ['guide', 'usher', 'follow']
        ]
    assert actual == expected
