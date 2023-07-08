q = int(input())

for _ in range(q):
    a, b, c = map(int, input().split())
    
    ans = []
    nom = abs(a-b) + abs(a-c) + abs(b-c)
    ans.append(nom)
    
    ax = [a-1, a, a+1]
    bx = [b-1, b, b+1]
    cx = [c-1, c, c+1]

    for i in ax:
        for j in bx:
            for k in cx:
                distance = abs(i-j) + abs(i-k) + abs(j-k)
                ans.append(distance)
    
    min_distance = min(ans)
    print(min_distance)
