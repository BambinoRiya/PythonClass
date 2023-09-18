t = int(input())
 
for _ in range(t):
    n = int(input())
    candies = list(map(int, input().split()))
 
    alice_weight = 0
    bob_weight = 0
    left = 0
    right = n - 1
    total_candies = 0
 
    while left <= right:
        if alice_weight < bob_weight:
            alice_weight += candies[left]
            left += 1
        else:
            bob_weight += candies[right]
            right -= 1
 
        if alice_weight == bob_weight:
            total_candies = left + (n - 1 - right)
 
    print(total_candies)
