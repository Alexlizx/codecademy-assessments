import gemstone

# Definition for singly-linked list node.
# class Gemstone:
#     def __init__(self, value, next_node=None):
#         self.value = value
#         self.next_node = next_node

# Write your code here
def remove_gem(gemstones, i):
    if i < 0:
        return gemstones
    if gemstones is None:
        return None
    if i == 0:
        return gemstones.next_node

    gemstones.next_node = remove_gem(gemstones.next_node, i - 1)
    return gemstones


# Test code, you don't need to edit
gem_list = gemstone.Gemstones(["Amber", "Sapphire", "Jade", "Pearl"])

head = gem_list.head
head = remove_gem(head, 1)

while head:
  if head.next_node:
    print(head.value, end='->')
  else:
    print(head.value)
  head = head.next_node