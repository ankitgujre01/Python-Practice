# Input: Number of terms
num = int(input("Enter the number : "))

a, b = 0, 1

if num <= 0:
    print("Please enter a positive integer.")
elif num == 1:
    print(a)
else:
    print(a, b, end=' ')
    for i in range(2, num):
        next_term = a + b
        print(next_term, end=' ')
        a, b = b, next_term
