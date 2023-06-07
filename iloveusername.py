n = int(input())  
 
points = list(map(int, input().split()))  
 
amazing_count = 0  
 
best_record = worst_record = points[0]
 
for i in range(1, n):
    if points[i] > best_record:
        best_record = points[i]
        amazing_count += 1
    elif points[i] < worst_record:
        worst_record = points[i]
        amazing_count += 1
 
print(amazing_count)
