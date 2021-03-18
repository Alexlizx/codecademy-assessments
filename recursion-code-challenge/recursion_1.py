# Write your code below
def move_amber(gemstones):
    result = []
    if len(gemstones) == 0:
        return result
        
    if gemstones[0] == 'Amber':
        result = move_amber(gemstones[1:])
        result += gemstones[0:1]
    else:
        result = gemstones[0:1]
        result += move_amber(gemstones[1:])

    return result

# Write your code below
gemstones = ['Jade', 'Amber', 'Jade', 'Pearl', 'Sapphire', 'Amber', 'Sapphire', 'Sapphire', 'Sapphire', 'Pearl']
print(move_amber(gemstones))