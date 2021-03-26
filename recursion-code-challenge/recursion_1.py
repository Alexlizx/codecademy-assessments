def move_to_end(lst, val):
  result = []
  if len(lst) == 0:
    return []
      
  if lst[0] == val:
    result = move_to_end(lst[1:], val)
    result += lst[0:1]
  else:
    result = lst[0:1]
    result += move_to_end(lst[1:], val)

  return result

# Test code, you do not need to edit
gemstones = ["Amber", "Sapphire", "Amber", "Jade"]
print(move_to_end(gemstones, "Amber"))