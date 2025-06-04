instructions = input()
letters = ""
while len(instructions) > 0:
    if instructions.find("+") > instructions.find("-") and instructions.find('-') > -1:
        print(f"{instructions[:instructions.find("-")]} loosen {instructions[instructions.find("-") + 1]}")
        instructions = instructions[instructions.find("-")+2:]
    else:
        print(f"{instructions[:instructions.find("+")]} loosen {instructions[instructions.find("+") + 1]}")
        instructions = instructions[instructions.find("+")+2:]
