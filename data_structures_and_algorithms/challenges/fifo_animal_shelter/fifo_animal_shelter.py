class Animal(object):
    def __init__(self,name, type = None, next = None):
        self.name = name
        self.type = type
        self.next = next


class AnimalShelter(object):
    def __init__(self):
        self.front = None
        self.rear = None
        self._length = 0

    def __str__(self):
        current = self.front
        output = 'Front -> '
        while current:
            output += f"{current.name} -> " 
            current = current.next
        output+="Rear"
        return output 



    def enqueue(self, name, type):
        try:
            if type == 'cat' or type == 'dog':
                to_add = Animal(name,type)
                if not self.front:
                    self.front = to_add
                else:
                    iter_animal = self.front

                    while iter_animal.next is not None:
                        iter_animal = iter_animal.next

                    iter_animal.next = to_add
                    self.rear = iter_animal
                self._length += 1
            
        except Exception as error:
            return f'Method has an error: {error}'

    def dequeue(self, preferred_animal=None):
        try:
            stop = True
            if self._length < 1:
                return('The queue is empty')

            if preferred_animal == 'dog' or preferred_animal == 'cat':

                iter_animal = self.front
                if self.front.type == preferred_animal:
                    self.front = self.front.next
                    stop = False
                while iter_animal.next.type is not None and stop:
                    if iter_animal.next.type == preferred_animal:
                        self._length -= 1
                        iter_animal.next = iter_animal.next.next
                        break
                    else:
                        iter_animal = iter_animal.next

            elif self.front.type == preferred_animal or preferred_animal is None:
                temp = self.front
                self.front = temp.next
                self._length -= 1
        except Exception as error:
            return f'Method has an error: {error}'







if __name__ == "__main__":
    animals = AnimalShelter()
    animals.enqueue('Cherry','cat')
    animals.enqueue('Oscar','dog')
    animals.enqueue('Bobi','dog')




    # cat.dequeue('dog')

    print(animals)