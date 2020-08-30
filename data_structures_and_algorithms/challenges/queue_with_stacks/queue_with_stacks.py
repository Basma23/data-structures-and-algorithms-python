class PseudoQueue():
    def __init__(self):
        self.items = []

    def enqueue(self, info):
        if info == None:
            return 'Uncorrect input'
        else:
            return self.items.insert(0, info)

    def dequeue(self):
        if len(self.items) == 0:
            return 'Empty'
        else:
            return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return 'Empty'
        else:
            return self.items[len(self.items) - 1]

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    pseudo_queue = PseudoQueue()
    pseudo_queue.enqueue(2)
    pseudo_queue.enqueue(4)
    pseudo_queue.enqueue(6)
    pseudo_queue.enqueue(8)
    print(pseudo_queue.items)
    pseudo_queue.dequeue()
    print(pseudo_queue.items)
    pseudo_queue.peek()
    print(pseudo_queue.items)

