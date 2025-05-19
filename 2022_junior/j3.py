instructions = input()
strings = ""
adjustment = ""
turns = 0
for i in instructions:
    if int(i) == int:
        turns = int(i)
        print(f"{strings} {adjustment} {turns}")
    if i == "-" or i == "+":
        adjustment = i
    else:
        strings = strings + i