from .LinkedList import LinkedList


def test_find():
    linked_list = LinkedList(1)
    for x in range(20):
        linked_list.append(x)
    assert linked_list.find(4) == 4
    assert linked_list.find(90) == None


def test_get_values():
    linked_list = LinkedList()
    for x in range(5):
        linked_list.append(x)
    assert linked_list.get_values() == list(range(5))


def test_remove():
    linked_list = LinkedList()
    for x in range(5):
        linked_list.append(x)
    linked_list.remove(3)
    assert linked_list.find(3) == None
    assert linked_list.get_values() == [0, 1, 2, 4]


def test_count():
    linked_list = LinkedList()
    for x in range(60):
        linked_list.append(x)
    assert linked_list.count() == 60


def test_pop():
    linked_list = LinkedList(2)
    assert linked_list.pop() == 2
    assert linked_list.count() == 0
    for x in range(4):
        linked_list.append(x)
    assert linked_list.pop() == 0
    assert linked_list.get_values() == [1, 2, 3]


def test_first():
    linked_list = LinkedList(2)
    assert linked_list.first() == 2
    assert linked_list.count() == 1
    for x in range(4):
        linked_list.append(x)
    assert linked_list.first() == 2
    assert linked_list.get_values() == [2, 0, 1, 2, 3]
