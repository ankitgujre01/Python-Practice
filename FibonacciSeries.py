n = int(input("Enter the number of terms: "))
def fabonacci(n):
    if n <= 1:
        return n
    else:
        return fabonacci(n - 1) + fabonacci(n - 2)

if n <= 0:
    print("Please enter a positive integer")
else:
    print("Fabonacci sequence:")
    for i in range(n):
        print(fabonacci(i))
        
    