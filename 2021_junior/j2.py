# Completed on 5/16/2025

number_of_bids = int(input())
highest = 0
winner = ""

for i in range(number_of_bids):
    name = str(input())
    bid = int(input())
    if bid > highest:
        highest = bid
        winner = name
        
print(winner)