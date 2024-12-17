def are_anagrams(str1, str2):
    # Convert both strings to lowercase to make the comparison case-insensitive
    str1 = str1.lower()
    str2 = str2.lower()
    
    # Sort the characters of both strings and compare
    return sorted(str1) == sorted(str2)

# Example usage
str1 = input("enter 1st string : ")
str2 = input("enter second string : ")

if are_anagrams(str1, str2):
    print(str1 ,"and", str2 , ' are anagrams.')
else:
    print(str1, "and", str2, ' are NOT anagrams.')
