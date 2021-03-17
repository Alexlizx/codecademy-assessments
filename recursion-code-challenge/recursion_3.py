# Write your code here

def generateFrame(n, gem):
    frame = ""

    if n <= 0:
        return gem

    frame += "<"
    frame += generateFrame(n-1, gem)
    frame += ">"

    return frame

print(generateFrame(3, "Pearl"))