# Completed on 6/11/2025

participants = int(input())
scores = []

for score in range(participants):
    score = int(input())
    scores.append(score)

scores.sort()
gold = scores[-1]
while scores[-1] == gold:
    scores.pop()
silver = scores[-1]
while scores[-1] == silver:
    scores.pop()
    
bronze_count = scores.count(scores[-1])

print(f" {scores[-1]} {bronze_count}")