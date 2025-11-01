weight = input("Enter your weight: ")
unit = input("(L)bs or (K)g: ")

if unit.upper() == "K":
    converted = float(weight) * 2.20462
    print(f"You are {converted:.2f} pounds")
elif unit.upper() == "L":
    converted = float(weight) * 0.453592
    print(f"You are {converted:.2f} kilograms")
else:
    print("Invalid unit")
