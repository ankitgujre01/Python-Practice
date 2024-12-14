string = input("Enter any string here: ").strip().lower()

if string == string[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
