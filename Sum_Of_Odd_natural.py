num = int(input("Enter any positive number: "))

if num < 0:
    print("Please enter a positive number.")
else:
    sum = 0
    
    while num > 0:
        if num % 2 != 0:
            sum += num
        num -= 1

    print("Sum of odd numbers =", sum)
