# Write your code here

def wrap_gem(gemstone, n):
    result = ""

    if n <= 0:
        return gemstone

    result += "<"
    result += wrap_gem(gemstone, n-1)
    result += ">"

    return result

print(wrap_gem("Pearl", 3))