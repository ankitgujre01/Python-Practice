num = int(input("Enter a number: "))

def sonn(n):
    if n <=1:
        return n
    else:
        return n + sonn(n - 1)

if num < 0:
    print("Please enter a positive integer")
elif num == 0:
    print("The sum of natural numbers from 1 to 0 is: 0")
else:    
    sum = sonn(num)
    print("The sum of natural numbers from 1 to", num, "is:", sum)