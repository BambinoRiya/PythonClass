# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
num = list(map(int, input().split()))

listA =[input() for _ in range(num[0])]
listB =[input() for _ in range(num[1])]

answer = defaultdict(list)

for i,word in enumerate(listA):
    answer[word].append(i+1)
    
for word in listB:
    if word in answer:
        print(" ".join(str(index)for index in answer[word]))
    else:
        print("-1")
