# size = int(input())
# arr = list(map(int, input().split()))

# if len(set(arr)) == 1:
#     print(size)
# else:
#     newArr = []
#     for i in range(size - 1):
#         if abs(arr[i] - arr[i+1]) <= 5:
#             newArr.append((arr[i], arr[i+1]))
#     print(len(set(newArr)) + 1)   BRUTE FORCE APPROACH HAHA

size = int(input())
arr = list(map(int, input().split()))

arr.sort()

max_students = 0
current_students = 0

left = 0
right = 0

while right < size:
    if arr[right] - arr[left] <= 5:
        current_students = right - left + 1
        max_students = max(max_students, current_students)
        right += 1
    else:
        left += 1

print(max_students)
