from .Stack import Stack


def test_push():
    stack = Stack()
    stack.push(2)
    assert stack.first() == 2


def test_pop():
    stack = Stack()
    stack.push(2)
    assert stack.pop() == 2
    assert stack.first() is None
