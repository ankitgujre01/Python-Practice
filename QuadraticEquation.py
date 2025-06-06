# formul ax^2 + bx + c = 0
# rules a, b, c are real numbers
# a != 0
import cmath

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

# discriminant fromula b^2 - 4ac
d = (b**2) - (4*a*c)

# formula of square root is -b ± √d / 2a

root1 = (-b - cmath.sqrt(d)) / (2*a)
root2 = (-b + cmath.sqrt(d)) / (2*a)

print("The roots are ", root1, "and", root2)