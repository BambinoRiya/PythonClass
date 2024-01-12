t = int(input())
 
for _ in range(t):
    num = int(input())
    items = list(map(int,input().split()))
 
    inc = 0
    dec = 0 
    flag = True 
 
    for x in range(1,num):
        if items[x] > items[x-1]:
            inc += 1
        elif items[x] < items[x-1]:
            dec += 1
            if inc > 0:
                flag = False
                break
    
    if flag == True:
        print("YES")
    else:
        print("NO")
