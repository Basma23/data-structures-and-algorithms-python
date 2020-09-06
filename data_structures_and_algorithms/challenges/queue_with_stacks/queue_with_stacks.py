from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues import Stack

class PseudoQueue():
    def __init__(self):
        self.front_stack = Stack()
        self.rear_stack = Stack()
        self.len = 0

    def enqueue(self, info):
        inputs = self.front_stack
        self.len += 1
        if info == None:
            return 'Not a valid input'
        inputs.push(info)
        return inputs

    def dequeue(self):
        if self.rear_stack.is_empty():
            while self.len > 0:
                self.rear_stack.push(self.front_stack.pop())
                self.len -= 1
            output = self.rear_stack.pop()

            while True:
                self.front_stack.push(self.rear_stack.pop())
                self.len += 1
                if self.rear_stack.is_empty():
                    return output

        else:
            return 'The stack is empty'

    def __str__(self):
        output = 'Rear -> '
        if self.front_stack.is_empty():
            current = self.rear_stack.top
        else:
            current = self.front_stack.top
        while current:
            output += f"{{{current.info}}} -> "
            current = current.next
        output+="Front"
        return output
        

if __name__ == '__main__':
    pseudo_queue = PseudoQueue()
    pseudo_queue.enqueue(2)
    pseudo_queue.enqueue(4)
    pseudo_queue.enqueue(6)
    pseudo_queue.enqueue(8)
    # pseudo_queue.dequeue()
    print(pseudo_queue)

