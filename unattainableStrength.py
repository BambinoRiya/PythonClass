n = int(input())
strengths = list(map(int, input().split()))
answer = 1
strengths.sort()
for s in strengths:
    if s <= answer:
        answer += s
    else:
        break
print(answer)
