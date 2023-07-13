
test_cases = int(input())

while test_cases:
    n = int(input())
    arr = list(map(int, input().split()))
    strenghts = arr.copy()

    strenghts.sort()

    for i in range(n):
        if arr[i] != strenghts[n - 1]:
            print(arr[i] - strenghts[n - 1], end=" ")
        else:
            print(arr[i] - strenghts[n - 2], end=" ")

    print()
    test_cases -= 1
