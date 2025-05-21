text = input()
happy = 0
sad = 0

for char in text:
    if char == ")":
        happy+=1
    elif char == "(":
        sad+=1
        
if happy > sad:
    print("happy")
elif sad > happy:
    print("sad")
elif happy == sad:
    print("unsure")
else:
    print("none")