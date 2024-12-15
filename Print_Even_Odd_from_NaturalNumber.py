while True:
    num = int(input("Enter the number of natural numbers: "))
    if num >= 0:
        break
    print("Please enter a positive number.")

even_numbers = []
odd_numbers = []

for i in range(1, num + 1):
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

print("Even numbers = ", even_numbers)
print("Odd numbers = ", odd_numbers)

