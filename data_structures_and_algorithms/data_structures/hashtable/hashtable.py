from data_structures_and_algorithms.data_structures.linked_list.linked_list import Node, LinkedList

class HashTable:
    def __init__(self, size=1024):
        self.map = [None] * size
        self.size = size
        self.current = None

    def hash(self, key):
        hashed_total = 0
        for char in key:
            hashed_total += ord(char)
        return hashed_total*19 % self.size

    def add(self, key, info):
        hashed_key = self.hash(key)
        contained = self.contains(key)
        if self.map[hashed_key] == None:
            self.map[hashed_key] = LinkedList()
        elif contained:
            self.current.info[1] = info
        return self.map[hashed_key].add((key, info))

    def get(self, key):
        hashed_key = self.hash(key)
        if self.map[hashed_key]:
            contained = self.contains(key)
            if contained:
                return self.current.info[1] 
        return 'Not in the table'

    def contains(self, key):
        hashed_key = self.hash(key)
        if self.map[hashed_key]:
            self.current = self.map[hashed_key].head 
            while self.current:
                if self.current.info[0] == key:
                    return True
                self.current = self.current.next
        return False

if __name__ == "__main__":
    table = HashTable()
    table.add('listen','listen value')
    table.add('silent','silent value')
    print(table.hash('listen'))
    print(table.map[table.hash('listen')].head.info[1])
    print(table.map[table.hash('silent')].head.next.info)
    print(table.get('listen'))
    print(table.get('listen'))
    print(table.get('silent'))
    print(table.get('speek'))
    print(table.contains('listen'))
    print(table.contains('silent'))
    print(table.contains('speek'))
