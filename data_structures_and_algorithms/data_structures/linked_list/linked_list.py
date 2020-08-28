class Node():
    def __init__(self, info):
        self.info = info
        self.next = None

class LinkedList():
    """
    Features of the linked list 
    Append
    Insert 
    Includes 
    Insert before a spicefic node
    Insert after a spicefic node
    Delete node
    Get kth from the end
    """

    # put your LinkedList implementation here
    def __init__(self, items = []):
        self.head = None
        for i in items:
            self.append(i)

    def append(self, info):
        new_node = Node(info)
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

    def insertBefore(self, targetValue, value):
        newNode = Node(value)
        node = self.head
        if node == None:
            return f'There aren\'t any nodes to insert before!'
        else:
            found = False
            while node:
                if node.next == None:
                    break
                if node.next.info == targetValue:
                    found = True
                    newNode.next = node.next
                    node.next = newNode
                    break
                else:
                    node = node.next
            if found != True:
                return 'Your target node of {} was not found in the list!'.format(targetValue)

    def insertAfter(self, prev_node, new_info):
        new_node = Node(new_info)
        old_node = self.head
        while old_node:
            if old_node.info == prev_node:
                new_node.next = old_node.next
                old_node.next = new_node
                return
            old_node = old_node.next

    def deleteNode(self, key):
        delete = self.head
        if (delete is not None):  
            if (delete.info == key):  
                self.head = delete.next
                delete = None
                return
        while(delete is not None):  
            if delete.info == key:  
                break
            prev = delete  
            delete = delete.next
        if(delete == None):  
            return
        prev.next = delete.next
  
        delete = None

    # def get_kth_from_end_ll(self, k):
    #     current = self.head
    #     length = 0
    #     while current is not None:
    #         current = current.next
    #         length += 1
    #         if k > length:
    #             return f'Location is greater than the' + ' length of LinkedList'
    #         current = self.head 
    #         for i in range(0, length - k): 
    #             current = current.next
    #         print(current.info)

    def get_kth_from_end_ll(self, k): 
        current = self.head  
        length = 0
        while current is not None: 
            current = current.next
            length += 1 
        if k > length: 
            print('Location is greater than the length of LinkedList') 
            return
        elif k < length: 
            print('Location is less than the length of LinkedList') 
            return
        current = self.head 
        for i in range(0, length - k): 
            current = current.next
        print(current.info) 

    def __str__(self):
        current = self.head
        output = ''
        while current: 
            output += f'{current.info} -> '
            current = current.next
        output += f'{current}'
        return output

if __name__=='__main__':
    drinks = LinkedList()
    drinks.append('Coffee')
    drinks.append('Ice_Tea')
    drinks.append('Lemonade')
    drinks.append('Mocha')
    drinks.insert('Milk')
    drinks.insertBefore('Mocha', 'milkcheck')
    drinks.insertAfter('Ice_Tea', 'Cocktail')
    # drinks.insertAfter(drinks.head.next.next, 'Water')
    drinks.deleteNode('Mocha')
    drinks.get_kth_from_end_ll(4) 
    print(f'{drinks}')

