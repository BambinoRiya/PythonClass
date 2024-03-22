def checkMultiples(curr):
    count =0 
    while curr%2==0:
        curr = curr//2
        count +=1
    return count
        
for _ in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))
    even = [n for n in range(1,n+1) if n%2==0]
    counter = 0
    
    for i in range(len(nums)):
        if nums[i]% 2==0:
            counter += checkMultiples(nums[i])
            continue
    
    need = n - counter
    even = [checkMultiples(n) for n in even]
    even.sort(reverse=True)

    count = 0
    curr = counter 
    
    if curr >= n:
        print(0)
        continue 
    flag = False   
    
    for i in range(len(even)): 
        curr += even[i]
        count +=1   
        if curr >= n:
            print(count)
            flag = True
            break
            
    if not flag:
        print(-1)  
