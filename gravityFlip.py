t = int(input())
newList = list(map(int, input().split()))

sortedList = sorted(newList)
print(' '.join(map(str, sortedList)))
