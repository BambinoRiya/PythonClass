t = int(input())
 
for _ in range(t):
    n, c = map(str, input().split())
    s = list(input())
    n = int(n)
    s += s
    res = 0
    count = 0
    
    flag = False
 
    for i in range(len(s)):
        if s[i] == c:
            flag = True
        if s[i] == 'g':
            flag = False
            res = max(res, count)
            count = 0
        if flag:
            count += 1
 
