def move_amber(gemstones):
  result = []
  if len(gemstones) == 0:
    return []
      
  if gemstones[0] == 'Amber':
    result = move_amber(gemstones[1:])
    result += gemstones[0:1]
  else:
    result = gemstones[0:1]
    result += move_amber(gemstones[1:])

  return result

# Test code, you do not need to edit
gemstones = ["Amber", "Sapphire", "Amber", "Jade"]
print(move_amber(gemstones))