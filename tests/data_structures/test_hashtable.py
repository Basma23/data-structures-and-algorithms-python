from data_structures_and_algorithms.data_structures.hashtable.hashtable import HashTable

def test_add_key_info():
    table = HashTable()
    table.add('adding','Add key and value')
    assert table.map[table.hash('adding')].head.info == ('adding','Add key and value')

def test_get_info_and_key():
    table = HashTable()
    table.add('Fruit','Mango')
    assert table.map[table.hash('Fruit')].head.info[0] == 'Fruit'
    assert table.map[table.hash('Fruit')].head.info[1] == 'Mango'

def test_get_info_from_key():
    table = HashTable()
    table.add('contain','listen')
    assert table.get('contain') == 'listen'

def test_get_info_not_in_table():
    table = HashTable()
    assert table.get('test') == 'Not in the table'

def test_handle_collision():
    table = HashTable()
    table.add('left','the building')
    table.add('felt','excited')
    hashed_key = table.hash('left')
    assert table.map[hashed_key].head.info == ('left','the building')
    assert table.map[hashed_key].head.next.info == ('felt','excited')

def test_retrieve_info_with_collision():
    table = HashTable()
    table.add('left','the building')
    table.add('felt','excited')
    assert table.get('left') == 'the building'
    assert table.get('felt') == 'excited'
