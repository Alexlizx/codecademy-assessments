# Write your code here

# Optimized recursive solution to calculate `pow(x, n)`
# using divide-and-conquer
def myPow(x, n):
    # base condition
    if n == 0:
        return 1
    # calculate subproblem recursively
    pow = myPow(x, n // 2)
 
    if n % 2 != 0:    # if `n` is odd
        return x * pow * pow
    else:             # otherwise, `n` is even
        return pow * pow

# Naive solution
# def myPow(x, n):
#     if n == 0:
#         return 1
#     elif n > 0:
#         return x * myPow(x, n-1)
#     else:
#         return (1/x) * myPow(x, n+1)

# Test code
print(myPow(2, 3))
print(myPow(-2, 3))