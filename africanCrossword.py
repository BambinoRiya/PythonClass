from collections import Counter

n, m = map(int, input().split())
arr = []

for _ in range(n):
    row = input().strip()
    arr.append(row)

duplicatesArr = arr.copy()
word = ""


for i in range(n):
    row = arr[i]
    count = Counter(row)  # {c:1, b:1, a:1}
    for j in range(m):
        if count[row[j]] > 1:
            duplicatesArr[i] = duplicatesArr[i][:j] + \
                "#" + duplicatesArr[i][j+1:]


for j in range(m):
    col = [arr[i][j] for i in range(n)]
    count = Counter(col)
    for i in range(n):
        if count[col[i]] > 1:
            duplicatesArr[i] = duplicatesArr[i][:j] + \
                "#" + duplicatesArr[i][j+1:]

for i in range(n):
    for j in range(m):
        if duplicatesArr[i][j] != "#":
            word += duplicatesArr[i][j]


print(word)
