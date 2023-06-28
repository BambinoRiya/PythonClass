n = int(input())
nums = list(map(int, input().split()))

mean = sum(nums) / n
counter = 0

indices = []  # List to store the indices

for i in range(len(nums)):
    if nums[i] == mean:
        counter += 1
        indices.append(i+1)  # Adding the index (i+1) to the list

print(counter)
for index in indices:
    print(index, end=' ')

# time complexity : O(n)
#space complexity : O(n)
