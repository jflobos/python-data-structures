class Stack:
    def __init__(self, value=None):
        self.next = None
        self.value = value
    
    def first(self):
        return self.value
    
    def pop(self):
        aux = self.value
        if self.next is not None:
            self.value = self.next.value
            self.next = self.next.next
        else:
            self.value = None
        return aux
    
    def push(self, value):
        if self.value is None:
            self.value = value
        else:
            if self.next is not None:
                self.next.push(value)
            else:
                self.next = Stack(value)