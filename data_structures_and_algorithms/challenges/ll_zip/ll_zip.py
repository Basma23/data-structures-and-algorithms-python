class Node():
    def __init__(self, info):
        self.info = info
        self.next = None

class LinkedList():
    """
    Features of the linked list 
    Zip the two linked lists together into one so that 
    the nodes alternate between the two lists and return 
    a reference to the head of the zipped list
    """

    # put your LinkedList implementation here
    def __init__(self):
        self.head = None

    def append(self, info):
        new_node = Node(info)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.info)
            current = current.next
        return elements

    def zip_lists(self, lists):
        current = self.head
        list_1 = lists.head
        list_2 = None

        if not current:
            return list_1
        if not list_1:
            return current

        if current and list_1:

            list_2 = current
            current = list_2.next

            new_head = list_2
        while current and list_1:
            list_2.next = list_1
            list_2 = list_1
            list_1 = list_2.next
            list_2.next = current
            list_2 = current
            current = list_2.next

        if not current:
            list_2.next = list_1
        if not list_1:
            list_2.next = current
        return new_head

if __name__ == '__main__':
    first = LinkedList()
    second = LinkedList()
    first.append(2)
    first.append(4)
    first.append(6)
    second.append(5)
    second.append(7)
    second.append(9)
    first.zip_lists(second)
    print(first.display())