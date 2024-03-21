for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().lstrip("0 ").split()))
    arr = arr[:-1]
    print(sum(arr)+ arr.count(0))
