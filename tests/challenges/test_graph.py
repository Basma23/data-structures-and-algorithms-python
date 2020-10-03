from data_structures_and_algorithms.challenges.graph.graph import *

def test_empty_nodes_for_graph():
    graph = Graph()
    actual = len(graph.get_nodes())
    expected = 0
    assert actual == expected
    
def test_add_node():
    graph = Graph()
    actual = graph.add_node('a').info
    expected = 'a'
    assert actual == expected

def test_add_edge():
    graph = Graph()
    start = graph.add_node('green')
    end = graph.add_node('red')
    graph.add_edge(start, end)
    assert graph._adjacency_list[start][0] == (end, 1)
    assert graph.get_neighbors(start) == [(end, 1)]
    graph.add_edge(end, start)
    assert graph.get_neighbors(end) == [(start, 1)]

def test_get_nodes():
    graph = Graph()
    first = graph.add_node('a')
    second = graph.add_node('b')
    third = graph.add_node('c')
    furth = graph.add_node('d')
    fifth = graph.add_node('e')
    actual = len(graph.get_nodes())
    expected = 5
    assert actual == expected

def test_get_neighbors():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    graph.add_edge(a, b, 4)
    neighbors = graph.get_neighbors(a)
    assert neighbors[0][0].info == 'b'
    assert len(neighbors) == 1
    assert neighbors[0][1] == 4


def test_size():
    graph = Graph()
    first = graph.add_node('a')
    second = graph.add_node('b')
    third = graph.add_node('c')
    furth = graph.add_node('d')
    fifth = graph.add_node('e')
    actual = graph.size()
    expected = 5
    assert actual == expected
