# Write your code here

def wrap_gem(gemstone, n):
    wrapped = ""

    if n <= 0:
        return gemstone

    wrapped += "<"
    wrapped += wrap_gem(gemstone, n-1)
    wrapped += ">"

    return wrapped

print(wrap_gem("Pearl", 3))