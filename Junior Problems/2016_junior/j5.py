question = int(input())
people = int(input())
country1 = input().split()
country2 = input().split()

country1.sort()
country2.sort()

def find_maximum(country1, country2):
    country1_2 = country1
    country2_2 = country2
    output1 = 0
    for i in range(people):
        lowest1 = int(country1.pop(0))
        highest2 = int(country2.pop(-1))
        output1+=max(lowest1,highest2)
        
    output2 = 0
    for i in range(people):
        highest1 = int(country1_2.pop(0))
        lowest2 = int(country2_2.pop(-1))
        output2+=max(highest1,lowest2)
        
    if output1 > output2:
        return output1
    else:
        return output2
    
    
def find_minimum(country1, country2):
    output = 0
    for i in range(people):
        lowest1 = int(country1.pop(0))
        lowest2 = int(country2.pop(0))
        output+=max(lowest1,lowest2)
    return output        
    
    

if question == 2:
    print(find_maximum(country1, country2))
else:
    print(find_minimum(country1, country2))