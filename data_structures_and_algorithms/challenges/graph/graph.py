from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues import Stack
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
        vertices = []
        depth = Stack()
        if start_node not in self._adjacency_list:
            raise ValueError
        depth.push(start_node)
        while not depth.is_empty():
           top_vertex = depth.pop()
           vertices.append(top_vertex.info)
           top_node_neighbors = self.get_neighbors(top_vertex)
           for neighbor in top_node_neighbors[::-1]:
               if not neighbor[0].visited_nodes:
                   top_vertex.visited_nodes = True
                   neighbor[0].visited_nodes = True
                   depth.push(neighbor[0])
        for node in self._adjacency_list:
            node.visited_nodes = False
        return vertices

    def get_edge(self, v_lst):
        def contains_vertex(value, lst):
            for vertex in lst:
                if isinstance(vertex, tuple):
                    if vertex[0].info == value:
                        return vertex
                    continue
                if vertex.info == value:
                    return vertex
            return False, 0
        current = contains_vertex(v_lst[0], self._adjacency_list.keys())
        if isinstance(current, Node):
            tsum = 0
            for index in range(1, len(v_lst)):
                current, cost = contains_vertex(v_lst[index], self.get_neighbors(current))
                tsum += cost
                if not current:
                    return (False, '$0')
            return (True, f'${tsum}')
        return (False, '$0')

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