size = int(input())

for _ in range(size):
    s = input()
    pointer1 = pointer2 = 0
    counts = [0, 0, 0]
    result = -1

    while pointer2 < len(s):   #112233  
        counts[int(s[pointer2]) - 1] += 1
        if all(counts):
            while all(counts):
                if result == -1 or pointer2 - pointer1 + 1 < result:
                    result = pointer2 - pointer1 + 1
                counts[int(s[pointer1]) - 1] -= 1
                pointer1 += 1
        pointer2 += 1

    print(result if result != -1 else 0)


'''
1    1    2    2    3    3
l,r

s[0]-1 



'''
