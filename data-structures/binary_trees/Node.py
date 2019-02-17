class Node:
    def __init__(self, value=None):
        self.value = value if value is not None else None
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value is None:
            self.value = value
        else:
            if self.value > value:
                self.left = self.__insert_into_branch(value, self.left)
            elif self.value < value:
                self.right = self.__insert_into_branch(value, self.right)
            else:
                raise ValueError('Same value insertion is not supported')

    def get_elements(self, elems=None):
        elems = [] if elems is None else elems
        if self.left is not None:
            elems = self.left.get_elements(elems)
        elems.append(self.value)
        if self.right is not None:
            elems = self.right.get_elements(elems)
        return elems

    def find(self, value):
        if value == self.value:
            return self
        elif value > self.value and self.right is not None:
            return self.right.find(value)
        elif self.left is not None:
            return self.left.find(value)
        return None

    def remove(self, value):
        node = self.find(value)
        if node is not None:
            node.__remove_from_tree(self)

    def __insert_into_branch(self, value, node):
        if node is not None:
            node.insert(value)
        else:
            node = Node(value)
        return node
