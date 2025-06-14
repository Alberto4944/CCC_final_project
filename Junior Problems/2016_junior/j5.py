question = int(input())
people = int(input())
country1 = input().split()
country2 = input().split()

country1.sort()
country2.sort()

def find_maximum(country1, country2):
    output1 = 0
    for i in range(people):
        lowest1 = int(country2.pop(0))
        highest2 = int(country1.pop(-1))
        output1+=max(lowest1,highest2)
        
        
    return output1
    
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