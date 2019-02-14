class LinkedList:
    def __init__(self, value=None):
        self.next = None
        self.value = value

    def append(self, value):
        if self.value is None:
            self.value = value
        else:
            if self.next is not None:
                self.next.append(value)
            else:
                self.next = LinkedList(value)
    
    def first(self):
        return self.value
    
    def pop(self):
        aux = self.value
        self.__replace_by_next()
        return aux

    
    def find(self, value):
        if self.value == value:
            return value
        elif self.next is not None:
            return self.next.find(value)
        else:
            return None

    def remove(self, value):
        if self.value == value:
            self.__replace_by_next()
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
    
    def __replace_by_next(self):
        if self.next is not None:
            self.value = self.next.value
            self.next = self.next.next
        else:
            self.value = None