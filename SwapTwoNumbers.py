# using third variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

temp = a
a = b
b = temp
print("After swapping, first number is: ", a)
print("After swapping, second number is: ", b)  

# using without third variable

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

x,y = y,x
print("After swapping, first number is: ", x)
print("After swapping, second number is: ", y)