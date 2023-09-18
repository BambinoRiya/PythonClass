n, t = map(int, input().split())
books = list(map(int, input().split()))
max_books = 0
prefix_sums = [0]
 
for time in books:
    prefix_sums.append(prefix_sums[-1] + time)
 
for i in range(n):
    l,r= 0,n
    while l < r:
        mid = l+(r-l) // 2
        mid += 1
        if prefix_sums[mid] - prefix_sums[i] <= t:
            l = mid
        else:
            r = mid - 1
    max_books = max(max_books, l - i)
 
print(max_books)
