test_cases = int(input())

for _ in range(test_cases):
    size = int(input())
    arr = list(map(int, input().split()))

    if size == 1:
        print("1 1")
        continue

    max_index = arr.index(max(arr))
    min_index = arr.index(min(arr))
    print(min_index + 1, max_index + 1)
