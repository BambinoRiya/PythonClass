n = int(input())
a = list(map(int, input().split()))

odd_nums, even_nums = 0, 0
for i in range(n):
    if a[i] % 2 ==0:
        even_nums += 1
    else:
        odd_nums += 1
        
if even_nums > 0 and odd_nums > 0:
    a.sort()
print(*a)
