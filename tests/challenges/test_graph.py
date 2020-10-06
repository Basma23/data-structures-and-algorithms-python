from data_structures_and_algorithms.challenges.graph.graph import *
import pytest

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
    graph.add_node('a')
    graph.add_node('b')
    graph.add_node('c')
    graph.add_node('d')
    graph.add_node('e')
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
    graph.add_node('a')
    graph.add_node('b')
    graph.add_node('c')
    graph.add_node('d')
    graph.add_node('e')
    actual = graph.size()
    expected = 5
    assert actual == expected

def test_breadth_first():
    g = Graph()
    a = g.add_node('a')
    b = g.add_node('b')
    c = g.add_node('c')
    g.add_edge(a,b,5)
    g.add_edge(b,c,2)
    g.add_edge(b,a,9)
    g.add_edge(c,a,5)
    assert g.bfs('a') == ['a','b','c']

def test_breadth_first_not_in_graph():
    g = Graph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    with pytest.raises(Exception):
        g.bfs('d')  

def test_breadth_first_start_from_end():
    g = Graph()
    a = g.add_node('a')
    b = g.add_node('b')
    c = g.add_node('c')
    g.add_edge(a,b,5)
    g.add_edge(b,c,1)
    g.add_edge(b,a,6)
    g.add_edge(c,a,9)
    assert g.bfs('c') == ['c','b','a']

def test_get_edges_one_vertex():
    g = Graph()
    v1 = g.add_node('Pandora')
    v2 = g.add_node('Mordor')
    v3 = g.add_node('Monstropolis')
    v4 = g.add_node('Metroville')
    v5 = g.add_node('Naboo')
    v6 = g.add_node('Narnia')
    g.add_edge(v1, v2, 110)
    g.add_edge(v2, v3, 50)
    g.add_edge(v2, v4, 12)
    g.add_edge(v3, v5, 43)
    g.add_edge(v4, v5, 23)
    g.add_edge(v4, v6, 14)
    g.add_edge(v5, v6, 21)
    actual = g.get_edge(['Mordor'])
    expected = (True, '$0')
    assert actual == expected

def test_get_edges_two_vertex():
    g = Graph()
    v1 = g.add_node('Pandora')
    v2 = g.add_node('Mordor')
    v3 = g.add_node('Monstropolis')
    v4 = g.add_node('Metroville')
    v5 = g.add_node('Naboo')
    v6 = g.add_node('Narnia')
    g.add_edge(v1, v2, 110)
    g.add_edge(v2, v3, 50)
    g.add_edge(v2, v4, 12)
    g.add_edge(v3, v4, 75)
    g.add_edge(v3, v5, 43)
    g.add_edge(v4, v5, 23)
    g.add_edge(v4, v6, 14)
    g.add_edge(v5, v6, 21)
    actual = g.get_edge(['Monstropolis', 'Metroville'])
    expected = (True, '$75')
    assert actual == expected

def test_three_vertex():
    g = Graph()
    v1 = g.add_node('Pandora')
    v2 = g.add_node('Mordor')
    v3 = g.add_node('Monstropolis')
    v4 = g.add_node('Metroville')
    v5 = g.add_node('Naboo')
    v6 = g.add_node('Narnia')
    g.add_edge(v1, v2, 110)
    g.add_edge(v2, v3, 50)
    g.add_edge(v2, v4, 12)
    g.add_edge(v3, v4, 75)
    g.add_edge(v3, v5, 43)
    g.add_edge(v4, v5, 23)
    g.add_edge(v4, v6, 14)
    g.add_edge(v5, v6, 21)
    actual = g.get_edge(['Pandora', 'Mordor', 'Monstropolis'])
    expected = (True, '$160')
    assert actual == expected

def test_false_get_edges():
    g = Graph()
    v1 = g.add_node('Pandora')
    v2 = g.add_node('Mordor')
    v3 = g.add_node('Monstropolis')
    v4 = g.add_node('Metroville')
    v5 = g.add_node('Naboo')
    v6 = g.add_node('Narnia')
    g.add_edge(v1, v2, 110)
    g.add_edge(v2, v3, 50)
    g.add_edge(v2, v4, 12)
    g.add_edge(v3, v4, 75)
    g.add_edge(v3, v5, 43)
    g.add_edge(v4, v5, 23)
    g.add_edge(v4, v6, 14)
    g.add_edge(v5, v6, 21)
    actual = g.get_edge(['Naboo, Pandora'])
    expected = (False, '$0')
    assert actual == expected