import math 
print("AREA CALCULATOR")
print("--------------------------------")
print(""" 
    press (1) to get the area of square
    press (2) to get the area of rectangle
    press (3) to get the area of circle
    press (4) to get the area of triangle
    """)


while True: 
    choice = input("Enter your choice: ")
    if choice.upper() == "Q":
        print("GOodBye")
        break 
    
    elif choice == "1": 
        side = float(input("Enter the side of the square: "))
        area = side ** 2
        
        print(f"the area of sqaure: {area}")
        
    elif choice == "2": 
        length = float(input("enter the length of rectangle: "))
        width = float(input("enter the width of reactangle: "))
        rectangle = length * width
        
        print(f"the area of ractangle: {rectangle}")
        
    elif choice == "3": 
        radious = float(input("enter the radius of the circle: "))
        area = math.pi * (radious **2)
        
        print(f"the area of circle: {area}")
        
    elif choice == "4": 
        base = float(input("enter the base of triangle: "))
        height = float(input("enter the height of triangle: "))
        area = 0.5 * base * height 
        
        print(f"the area of triangle: {area}")
        
    else : 
        print("invalid input")
    
    