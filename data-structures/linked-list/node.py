class LinkedList:
    def __init__(self, value=None):
        self.next = None
        self.value = value

    def insert(self, value):
        if self.next != None:
            self.next.insert(value)
        else:
            self.next = LinkedList(value)
    
    def find(self, value):
        if self.value == value:
            return value
        elif self.next is not None:
            return self.next.find(value)
        else:
            return None

    def remove(self, value):
        if self.value == value:
            if self.next is not None:
                self.value = self.next.value
                self.next = self.next.next
            else:
                self.value = None
                self.next = None
        elif self.next is not None:
            return self.next.remove(value)
       
    
    def get_values(self, values = None):
        if values is None:
            values = []
        if self.value is not None:
            values.append(self.value)
        if self.next is not None:
            return self.next.get_values(values)
        else:
            return values
    
    def print_values(self):
        print(self.value)
        if self.next is not None:
            self.next.print_values()
        
    
    def count(self, count = 0):
        if self.value is not None:
            count += 1
        if self.next is not None:
            return self.next.count(count)
        return count