bill = float(input(" please enter your bill = "))
persons = float(input(" How many persons you are = "))
tip = float(input("Tip % you want to give = "))
finalBill = bill + (tip/100)*bill
share = finalBill/persons

print("your final bill = ",finalBill)
print("Individual Share = ", share)
