def is_harshad_number(num):
    digit_sum = 0
    temp = num
    while temp > 0:
        digit_sum += temp % 10
        temp //= 10
    if num % digit_sum == 0:
        return True
    else:
        return False

# Example usage
num = int(input("Enter a positive integer: "))

if is_harshad_number(num):
    print(num, " is a Harshad number.")
else:
    print(num," is NOT a Harshad number.")
