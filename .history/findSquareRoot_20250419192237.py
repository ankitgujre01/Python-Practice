import math

n = float(input("Enter a number: "))

# print("The square root of", n, "is", n**(1/2))

# using math module
squareRoot = math.sqrt(n)
print("The square root of", n, "is", squareRoot)

# using function

def findSquareRoot(n):
    sqrt = 