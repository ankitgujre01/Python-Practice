num = int(input("Enter any positive number : "))

if num<0:
    print("Please enter Positive Number :")
else:
    sum = 0
    
    while num>0:
        sum += num
        num -= 1
    print(sum)