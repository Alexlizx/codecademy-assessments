import LinkedList

# Definition for singly-linked list node.
# class ListNode:
#     def __init__(self, value, next_node=None):
#         self.value = value
#         self.next_node = next_node

# Write your code here
def remove_node(head, i):
    if i < 0:
        return head
    if head is None:
        return None
    if i == 0:
        return head.next_node

    head.next_node = remove_node(head.next_node, i - 1)
    return head


# Test code, you don't need to edit
gemstones = LinkedList.LinkedList(["Amber", "Sapphire", "Jade", "Pearl"])

head = gemstones.head
head = remove_node(head, 1)
head.flatten()

