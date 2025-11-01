letter = input("enter the letters: ")

vowels = 0 
consonents = 0 

for i in letter:
    if i in "aeiouAEIOU":
        print(f"{i} is vowel")
        
        vowels += 1
        
    elif i.isalpha():
        print(f"{i} is consonent")
        
        consonents += 1 
        
    
print(f"total vowels: {vowels}")
print(f"total consonents: {consonents}")
