from collections import Counter

total_words = int(input())
givenList = []

for _ in range(total_words):
    words = input()
    givenList.append(words)
    

count = Counter(givenList) 

distinctList = []

for word in givenList:
    if count[word] > 0:  
        distinctList.append(count[word])
        count[word] =-1
        
print(len(distinctList))
print(*distinctList)


  
    
