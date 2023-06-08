from collections import Counter

x = int(input())  # total number of shoes
shoeList = list(map(int, input().split()))
counter = Counter(shoeList)

customerTotal = int(input())

amountEarned = 0
for _ in range(customerTotal):
    shoe, price = map(int, input().split())

    if counter[shoe] > 0:
        counter[shoe] -= 1
        amountEarned += price

print(amountEarned)
