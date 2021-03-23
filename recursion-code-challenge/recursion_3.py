def wrap_gem(gemstone, n):
  result = ""
  if n <= 0:
    return gemstone
  result += "<"
  result += wrap_gem(gemstone, n-1)
  result += ">"

  return result

# Test code, you do not need to edit
wrapped = wrap_gem("Pearl", 3)
print(wrapped)