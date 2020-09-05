from data_structures_and_algorithms.challenges.fifo_animal_shelter.fifo_animal_shelter import Animal, AnimalShelter

def test_enqueue():
    animals = AnimalShelter()
    animals.enqueue('Cherry','cat')
    expected = 'Cherry'
    actual = animals.front.name
    assert actual == expected


def test_last_enqueue():
    animals=AnimalShelter()

    animals.enqueue('Cherry','cat')
    animals.enqueue('Oscar','dog')
    animals.enqueue('Bobi','dog')

    expected = 'Front -> Cherry -> Oscar -> Bobi -> Rear'
    actual = animals.__str__()
    assert actual == expected

def test_dequeue_first_object():
    animals = AnimalShelter()

    animals.enqueue('Cherry','cat')
    animals.enqueue('Oscar','dog')
    animals.enqueue('Bobi','dog')
    animals.dequeue('Cat')
    expected ='Front -> Oscar -> Bobi -> Rear'
    actual = animals.__str__()
    assert actual == expected



def test_dequeue_second_object():
    animals = AnimalShelter()

    animals.enqueue('Cherry','cat')
    animals.enqueue('Oscar','dog')
    animals.enqueue('Bobi','dog')

    animals.dequeue('dog')
    expected = 'Front -> Cherry -> Bobi -> Rear'
    actual = animals.__str__()
    assert actual == expected






def test_dequeue_None():
    animals = AnimalShelter()

    expected = 'The queue is empty'
    actual = animals.dequeue('cat')
    assert actual == expected