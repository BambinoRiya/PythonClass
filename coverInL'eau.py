from collections import Counter
t = int(input())

for _ in range(t):
    n = int(input())
    s = list(input())  
    counted = Counter(s)
    count = 0
    
    for i in range(1, n - 1):
        if s[i] == '.' and s[i - 1] == '.' and s[i + 1] == '.':
            print(2)
            break
    else:
        print(counted['.'])
             
    
   
