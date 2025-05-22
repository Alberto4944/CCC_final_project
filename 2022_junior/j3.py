instructions = input()
strings = ""
adjustment = ""
turns = 0
for i in instructions:
    if int(i) == int:
        turns = int(i)
        print(f"{strings} {adjustment} {turns}")
    elif i == "-":
        adjustment = "loosen"
    elif i == "+":
        adjustment = "tighten"
    else:
        strings = strings + i