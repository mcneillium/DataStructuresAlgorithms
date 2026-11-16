import pytest

from graphs.graph import Graph
from hash_tables.hash_table import HashTable
from trees.binary_tree import BinaryTree


def test_inorder_traversal_is_sorted():
    t = BinaryTree()
    for k in [50, 30, 70, 20, 40, 60, 80]:
        t.insert(k)
    assert t.inorder_traversal() == [20, 30, 40, 50, 60, 70, 80]


def test_empty_tree():
    assert BinaryTree().inorder_traversal() == []


def test_bfs_visits_level_by_level():
    g = Graph()
    for u, v in [(0, 1), (0, 2), (1, 3), (2, 4)]:
        g.add_edge(u, v)
    assert g.bfs(0) == [0, 1, 2, 3, 4]


def test_bfs_handles_target_only_and_large_vertices():
    # Used to raise IndexError: vertex 5 only appears as an edge target.
    g = Graph()
    g.add_edge(1, 5)
    assert g.bfs(1) == [1, 5]


def test_bfs_handles_cycles_and_strings():
    g = Graph()
    g.add_edge("a", "b")
    g.add_edge("b", "a")
    assert g.bfs("a") == ["a", "b"]


def test_hash_table_keeps_colliding_keys():
    # "ab" and "ba" have the same hash; both must survive.
    t = HashTable()
    assert t.get_hash("ab") == t.get_hash("ba")
    t["ab"] = 1
    t["ba"] = 2
    assert t["ab"] == 1 and t["ba"] == 2


def test_hash_table_update_delete_and_missing():
    t = HashTable()
    t["k"] = 1
    t["k"] = 2
    assert t["k"] == 2
    assert "k" in t
    del t["k"]
    assert "k" not in t
    with pytest.raises(KeyError):
        _ = t["k"]


def test_tree_layout_places_children_either_side_of_parent():
    from trees.binary_tree import BinaryTree, layout

    t = BinaryTree()
    for v in [50, 30, 70, 20]:
        t.insert(v)
    nodes, edges = layout(t)
    pos = {v: (col, depth) for v, col, depth in nodes}
    assert pos[50][1] == 0 and pos[30][1] == 1 and pos[20][1] == 2
    assert pos[20][0] < pos[30][0] < pos[50][0] < pos[70][0]
    names = [n[0] for n in nodes]
    assert {(names[a], names[b]) for a, b in edges} == {(50, 30), (50, 70), (30, 20)}


def test_graph_nodes_include_edge_targets():
    from graphs.graph import Graph

    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(1, 4)
    assert set(g.nodes()) == {0, 1, 4}
    assert g.bfs(4) == [4]  # a node with no outgoing edges is still searchable
