test_cases = int(input())

for _ in range(test_cases):
    num_elements = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    
    left = 0
    right = num_elements - 1
    amt = 0
    
    while right > left:
        amt += arr[right] - arr[left]
        right -= 1
        left += 1
        
    print(amt)
