n = int(input("Enter a number: "))

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)
if n <= 0:
    print("Please enter a positive integer")
else:
    factorial = fact(n)
    print("The factorial of", n, "is:", factorial)