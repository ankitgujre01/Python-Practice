num = int(input("Enter any Numbers : "))
sum = 0
order = len(str(num))
copy_num = num
while(num>0):
    digit = num%10
    sum += digit ** order
    num =num//10
    
if(sum == copy_num):
    print(f"{copy_num} is an armstrong Nmber.")
else:
    print(f"{copy_num} is not an armstrong number")
