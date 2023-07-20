test_cases = int(input())

while test_cases:
    n = int(input())
    oldArr = list(map(int, input().split()))

    left = 0
    right = n - 1
    newArr = [0] * n

    if n == 1:
        print(' '.join(map(str, oldArr)))
        test_cases -= 1
        continue

    index = 0
    while right >= left:
        if index < n:
            newArr[index] = oldArr[left]
            index += 1
        if index < n:
            newArr[index] = oldArr[right]
            index += 1
        left += 1
        right -= 1

    print(' '.join(map(str, newArr)))

    test_cases -= 1
