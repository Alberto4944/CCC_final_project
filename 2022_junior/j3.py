instructions = input()

    
def action(loosen, tighten, instructions):
    if loosen < tighten and loosen != -1:
        print(f"{instructions[:loosen]} loosen {instructions[loosen + 1]}")
        instructions = instructions[loosen+2:]
    else:
        print(f"{instructions[:tighten]} tighten {instructions[tighten + 1]}")
        instructions = instructions[tighten+2:]
    return instructions
        
while len(instructions) > 0:
    try:
        loosen = instructions.index("-")
    except:
        print(f"{instructions[:-1]} loosen {instructions[-1]}")
        instructions = instructions[loosen+2:]
    
    try:
        tighten = instructions.index("+")
    except:
        print(f"{instructions[:-1]} tighten {instructions[-1]}")
        instructions = instructions[tighten+2:]
        
    instructions = action(loosen,tighten,instructions)