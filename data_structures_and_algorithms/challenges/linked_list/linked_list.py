class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def insert(self, info):
        new_node = Node(info)
        new_node.next = self.head
        self.head = new_node

    def includes(self, info):
        current = self.head
        while current:
            if info == current.info:
                print('True')
                return True
            else: current = current.next
        print('False')
        return False

    def __str__(self):
        current = self.head
        output = ''
        while current: 
            output += f'<{current.info} ->'
            current = current.next
        output += f'{current}'
        return output

    def insert_between(self, prev_info, info):
        try:
            do
        except:
            return ('This function doesn\'t have been initialized yet')

