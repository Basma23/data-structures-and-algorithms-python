class Node():
    def __init__(self, info):
        self.info = info
        self.next = None

class Stack():
    def __init__(self):
        self.top = None
        self.items = []

    def push(self, info):
        if self.top == None:
            self.top = Node(info)
            self.items.append(info)
        else:
            new_node = Node(info)
            self.top.next = new_node
            self.top = new_node
            self.items.append(new_node.info)

    def pop(self):
        if self.top:
            popped = self.top
            self.top = self.top.next
            return popped.info
        else:
            return f'the stack is empty'

    def peek(self):
        try:
            return self.top.info
        except AttributeError as error:
            return 'the stack is empty'

    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False

class Queue():
    def __init__(self):
        self.front = None
        self.rear = None
        self.items = []

    def enqueue(self, info):
        new_node = Node(info)
        if not self.front and not self.rear:
            self.front = new_node
            self.rear = new_node
            self.items.append(new_node.info)
            return
        old_rear = self.rear
        self.rear = new_node
        self.items.append(new_node.info)

    def dequeue(self):
        try:
            temp = self.front
            self.front = temp.next
            if self.front == None:
               self.rear = None
            self.items.pop(0)
            return temp.info
        except AttributeError as e:
            return 'the queue is empty'

    def peek(self):
        try:
            return self.front.info
        except AttributeError as error:
            return 'the queue is empty'

    def is_empty(self):
       if not self.front:
           return True
       else :
           return False

if __name__ == '__main__':
    fruites = Stack()
    fruit = Queue()
    # fruites.push('Orange')
    # fruites.push('Pineapple')
    # fruites.push('Berry')
    # print(fruites.items)
    # # print(fruites.peek())
    # print(fruites.pop())
    # print(fruites.items)
    fruit.enqueue('Mango')
    fruit.enqueue('Strawberry')
    fruit.enqueue('Peach')
    print(fruit.items)
    print(fruit.front.info)
    print(fruit.rear.info)
    print(fruit.peek())
    print(fruit.dequeue())

