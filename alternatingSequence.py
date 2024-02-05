testcases = int(input())

for _ in range(testcases):
    n = int(input())
    arr = list(map(int, input().split()))
    
    
    # next_ptr = 0
    max_ptr = arr[0]
    sum_count = 0
    
    
    for i in range(1,n):
        if arr[i]*max_ptr<0:
            sum_count +=max_ptr
            max_ptr = arr[i]
        else:
            max_ptr = max(max_ptr,arr[i])
    print(sum_count + max_ptr)
    
    
