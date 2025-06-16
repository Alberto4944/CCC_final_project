# Completed on 6/3/2025

text = input()
string = input()

# Does a shift
def cyclic(text,string):
    new_text = text
    for shift in range(len(text)):
        for char in range(len(new_text)):
            if new_text[char] == string[0] and new_text[char:char+len(string)] == string:
                return "yes"
        string = string[1:]+string[0]
    return "no"

print(cyclic(text,string))