for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    res = []
    
    for i in range(n):
        res.append((n+1)-arr[i])
        
    print(*res)
