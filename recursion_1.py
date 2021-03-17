# Write your code below
def move_amber(gemstones):
    if len(gemstones) == 0:
        return []
    if gemstones[0] == 'Amber':
        return move_amber(gemstones[1:]) + gemstones[0:1]
    else:
        return gemstones[0:1] + move_amber(gemstones[1:])


# Write your code below
gemstones = ['Jade', 'Amber', 'Jade', 'Pearl', 'Sapphire', 'Amber', 'Sapphire', 'Sapphire', 'Sapphire', 'Pearl']
print(move_amber(gemstones))