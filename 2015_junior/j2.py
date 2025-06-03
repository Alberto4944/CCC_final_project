# Completed on 6/2/2025

text = input()
happy = 0
sad = 0

for index in range(len(text)):
    if text[index] == ":" and text[index+1] == "-":
        if text[index+2] == ")":
            happy+=1
        elif text[index+2] == "(":
            sad+=1
        
if happy > sad:
    print("happy")
elif sad > happy:
    print("sad")
elif happy == sad and happy > 0 and sad > 0:
    print("unsure")
else:
    print("none")