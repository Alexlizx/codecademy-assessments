# Definition for singly-linked list node.
class Gemstone:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

# Behind the scene linked-list class
class Gemstones:
    def __init__(self):
        self.head = None
    def __init__(self, lst):
        self.head = Gemstone(lst[0])
        current = self.head
        for val in lst[1:]:
            current.next_node = Gemstone(val)
            current = current.next_node
    def append(self, value):
        temp = Gemstone(value)
        if self.head is None:
            self.head = temp
            return
        
        last = self.head
        while last.next_node:
            last = last.next_node
        last.next_node = temp
        