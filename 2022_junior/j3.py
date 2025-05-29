instructions = input()
numbers = "0123456789"

for char in range(len(instructions)):
    strings = ""
    times = 0
    if instructions[char] == "+":
        times = int(instructions[char + 1])
        print(f"{strings} tighten {times}")
        strings = ""
        times = ""
    elif instructions[char] == "-":
        print(f"{strings} tighten {times}")
        strings = ""
        times = ""
    else:
        strings+=char
        