# Completed on 5/16/2025

players = int(input())
gold = True
good_players = 0
for i in range(players):
    score = int(input())
    fouls = int(input())
    if (score * 5) - (fouls * 3) > 40:
        good_players+=1
    else:
        gold = False
if gold:
    print(f"{good_players}+")
else:
    print(good_players)