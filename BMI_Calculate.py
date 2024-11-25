''' Bmi Calcilator'''
# formula BMI = Weight(in kg) / height * height(in meters)

weight = float(input("Enter your weight in kg "))
height = float(input("Enter your height in meters "))

bmi = weight/height**2
print(bmi)