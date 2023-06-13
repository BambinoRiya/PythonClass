t = int(input())
 
for _ in range(t):
    a1, b1 = map(int, input().split())
    a2, b2 = map(int, input().split())
    a = max(a1, b1)
    b = min(a1, b1)
    if a == a2:
        c = b2
    elif a == b2:
        c = a2
    else:
        print("No")
        continue
 
    if a == b + c:
        print("Yes")
    else:
        print("No")
