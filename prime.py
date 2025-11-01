def prime_check(number):
    
    if number < 2:
        return False 
    if number == 2:
        return True 
    if number % 2 == 0:
        return False 
    i = 3 
    while i * i <= number:
        if number % i == 0:
            return False 
        i += 2 
    return True 


while True:
    number_input = input("Enter a number: ")
    
    if number_input.upper() == "Q":
        print("GOODBYE!")
        break
    
    try: 
        number = int(number_input)
        
        if prime_check(number):
            print(f"{number} is A PRIME number")
            
        else:
            print(f"{number} is NOT A PRIME number")
            
    except ValueError:
        print("INVALID INPUT")
        
        
    print("--------------------------------")
    
    