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
        res = gemstones.next_node
        return res

    gemstones.next_node = remove_gem(gemstones.next_node, i - 1)
    return gemstones


# Behind the scene test code
gemstone_list = ['Jade', 'Jade', 'Pearl', 'Sapphire', 'Sapphire', 'Sapphire', 'Sapphire', 'Pearl', 'Amber', 'Amber']
container = gemstone.Gemstones()

for gem in gemstone_list:
    container.append(gem)

head = container.head
head = remove_gem(head, 2)
while head:
    print(head.value, end=' ')
    head = head.next_node
