t = int(input())

for _ in range(t):
    num = int(input())
    list1 = list(map(int,input().split()))
    list2 = list(map(int,input().split()))
    sort1 = sorted(list1)
    sort2 = sorted(list2)
 
    for i in range(len(sort1)):
        if sort1[i] != sort2[i]:
            sort1[i] += 1
 
    if sort1 == sort2:
        print("YES")
    else:
        print("NO")
      
