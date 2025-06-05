word = input()

for char in range(len(word)):
    reverse = char
    letters = ""
    for i in word[char:]:
        i+=reverse
        reverse = reverse