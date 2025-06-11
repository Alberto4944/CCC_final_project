original = input()
altered = input()
silly_key = ""

for char in range(len(original)):
    if original[:char+1] != altered[:char+1] and original.count(original[char]) != (len(original) - len(altered)):
        print(original[char])
        break
        
    
        
print(len(altered) - len(original))