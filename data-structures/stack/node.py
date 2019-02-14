class Stack:
    def __init__(self, value=None):
        self.next = None
        self.value = value
    
    def test(self):
        print self.value