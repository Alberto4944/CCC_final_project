# Completed on 6/9/2025

instructions = input()
number_list = "0123456789"

def do_thing(instructions):
    numbers = ""
    for char in range(len(instructions)):
        if instructions[char] == "+":
            for number in instructions[char+1:]:
                if number in number_list:
                    numbers+=number
                else:
                    break
            print(f"{instructions[:char]} tighten {numbers}")
            return instructions[char+len(numbers)+1:]
        elif instructions[char] == "-":
            for number in instructions[char+1:]:
                if number in number_list:
                    numbers+=number
                else:
                    break
            print(f"{instructions[:char]} loosen {numbers}")
            return instructions[char+len(numbers)+1:]

while len(instructions) > 0:
    instructions = do_thing(instructions)