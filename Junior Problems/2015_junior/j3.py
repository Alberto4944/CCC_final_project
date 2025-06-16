# Completed on 6/13/2025

text = input()

consonants = "bcdfghjklmnpqrstvwxyz"
result = ""

# Find nearest vowel next to the consonant
def find_nearest_vowel(consonant):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    lowest_distance = 26
    for vowel in "aeiou": # Checks the distance between each vowel and the consonant
        distance = abs(alphabet.index(consonant) - alphabet.index(vowel))
        if distance < lowest_distance:
            closest_vowel = vowel
            lowest_distance = distance
    return closest_vowel

# Finds the next consonant
def find_next_consonant(consonant):
    consonants = "bcdfghjklmnpqrstvwxyz"
    if consonant == "z":
        return consonant
    else:
        return consonants[consonants.index(char)+1] 

# Checks the text for each consonant and does each function
for char in text:
    if char in consonants:
        result+=char + find_nearest_vowel(char) + find_next_consonant(char)
    else:
        result+=char
        
print(result)