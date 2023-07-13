from collections import defaultdict
t = int(input())
 
for _ in range(t):
    n,c =  map(int,(input().split()))
    lists = list(map(int, input().split()))
 
    hashmap = defaultdict(int)
    count = 0
 
    for x in range(len(lists)):
        hashmap[lists[x]] += 1
        if hashmap[lists[x]] <= c:
            count += 1
    print(count)
