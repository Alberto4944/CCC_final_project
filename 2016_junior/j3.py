word = input()
longest = 0

def reverse_chars(characters):
	output = ""
	for character in characters:
		output = character + output
	return output

for letter in range(len(word)):
	slice = word[letter:]
	for i in range(len(slice)):
		chars = slice[:i+1]
		if chars == (reverse_chars(chars)) and len(chars) > longest:
			longest = len(chars)
			
print(longest)