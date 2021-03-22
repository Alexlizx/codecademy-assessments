# Definition for singly-linked list node.
class Gemstone:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

# Behind the scene linked-list class
class Gemstones:
    def __init__(self):
        self.head = None
    def append(self, value):
        temp = Gemstone(value)
        if self.head is None:
            self.head = temp
            return
        
        last = self.head
        while last.next_node:
            last = last.next_node
        last.next_node = temp
    def copy(self, list):
        for gem in list:
            self.append(gem)

        return self.head