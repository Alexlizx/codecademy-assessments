# Definition for singly-linked list node.
class ListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    def flatten(self):
        temp = self
        while temp:
            if temp.next_node:
                print(temp.value, end='->')
            else:
                print(temp.value)
            temp = temp.next_node

# Behind the scene linked-list class
class LinkedList:
    def __init__(self):
        self.head = None
    def __init__(self, lst):
        self.head = ListNode(lst[0])
        current = self.head
        for val in lst[1:]:
            current.next_node = ListNode(val)
            current = current.next_node
    def append(self, value):
        temp = ListNode(value)
        if self.head is None:
            self.head = temp
            return
        
        last = self.head
        while last.next_node:
            last = last.next_node
        last.next_node = temp
        