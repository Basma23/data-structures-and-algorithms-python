class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Dog:
    def __init__(self, name):
        self.name = name

class Cat:
    def __init__(self, name):
        self.name = name    

class AnimalShelter:

    def __init__(self):
        self.front = None
        self.rear = None
        self.next = None

    def enqueue(self, obj):
        
        node = Node(obj)
        if not self.front and not self.rear:
            self.front = node
            self.rear = node

        old_rear = self.rear
        self.rear = node
        old_rear.next = self.rear


    def dequeue(self,pref):
        try:
            self.front
        except AttributeError:
            return "Queue Is Empty"
        else:
            if pref == 'cat':
                temp = self.front
                curr = temp.next
                # print(curr)
                while temp:
                    # print('*********** Here **********')
                    if type(temp.value) == type(Cat('Sherry')):
                        print('*********** Here **********')
                        droped = temp.value
                        temp = temp.next
                        return droped
                        break
                    temp = temp.next
                    # curr = curr.next
            else:
                return None


    def __str__(self):

        current = self.front
        # output = 'rear->'
        output = ''
        while current:
            output += f"{current.value}->"
            current = current.next
        # output+="<-front"
        return output 

if __name__ == "__main__":
    alex = Dog('Alex')
    boby = Dog('Boby')
    jou = Dog('Jou')
    animals = AnimalShelter()
    animals.enqueue(alex)
    animals.enqueue(boby)
    animals.enqueue(jou)
    print(animals.dequeue('cat'))
    print(animals.__str__())