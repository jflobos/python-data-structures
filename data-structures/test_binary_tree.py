import pytest
from binary_trees.Node import Node


def test_insert():
    tree = Node()
    elems = [1, 4, 6, 2, 3, 65, 31, 89, 5, 7, 8]
    for elem in elems:
        tree.insert(elem)
    assert(tree.get_elements() == sorted(elems))


def test_should_throw_exceptions():
    with pytest.raises(ValueError):
        tree = Node(1)
        tree.insert(1)


def test_find():
    tree = Node()
    elems = [1, 4, 6, 2, 3, 65, 31, 89, 5, 7, 8]
    for elem in elems:
        tree.insert(elem)
    assert(tree.find(89).value == 89)
    assert(tree.find(100) == None)
