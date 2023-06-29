t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    if (n % 2 == 0 or k == 1): #n=5, k=3
        print("YES")
        continue
    if (k % 2 == 0 and n % 2 == 1):
        print("NO")
        continue
    if (n < k):
        print("NO")
        continue
    print("YES")
    
#Time complexity : O(t)
#space complexity : O(1)
