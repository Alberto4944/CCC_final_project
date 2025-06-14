start = input().split()
x1 = int(start[0])
y1 = int(start[1])

end = input().split()
x2 = int(end[0])
y2 = int(end[1])

electricity = int(input())

# Distance away (right angle turns)
distance = abs(x2-x1)+abs(y2-y1)

# Basically, the amount of electricity has to be at least the distance amount. But also, if the distance is even, the electiricty has to be even. If odd, the same thing. That's because everything has the opposite effect, say you make a uturn in a straight path to the finish then turn back. That was two turns.

if electricity >= distance and (electricity % 2 and distance % 2 or not electricity % 2 and not distance % 2):
    print("Y")
else:
    print("N")