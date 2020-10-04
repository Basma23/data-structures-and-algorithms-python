# from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues import *
from queue import Queue

class Node:
    def __init__(self, info):
        self.info = info

class Graph():
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, info):
        node = Node(info)
        self._adjacency_list[node] = []
        return node

    def add_edge(self, start_node, end_node, weight=1):
        add_edge = self._adjacency_list[start_node]
        add_edge.append((end_node, weight))
        return add_edge

    def get_nodes(self):
        return self._adjacency_list.keys()

    def get_neighbors(self, node):
        return self._adjacency_list[node]

    def size(self):
        return len(self._adjacency_list)

    def bfs(self, start_node):
        q = Queue()
        q.enqueue(start_node)
        visited_nodes = {}
        visited_nodes[start_node] = True
        result = []
        while len(q):
            current = q.dequeue()
            result.append(current)
            neighbors = self._adjacency_list[current]
            for n in neighbors:
                if n[0] not in visited_nodes:
                    q.enqueue(n[0]) 
                visited_nodes[n[0]] = True
        return result

    def dfs(self, start_node):
        pass

if __name__ == "__main__":
    g = Graph()
    print(g._adjacency_list)
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    print(g.get_nodes())
    print(g.size())

    # Not best practice for testing, but only for bfs
    a = Node('a')
    b = Node('b')
    c = Node('c')
    g._adjacency_list[a] = [b, c]
    g._adjacency_list[b] = [a, c]
    g._adjacency_list[c] = [a, b]
    print(g.bfs(a))