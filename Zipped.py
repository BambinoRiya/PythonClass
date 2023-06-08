studentTotal, subjectTotal = map(int, input().split())
result =[]

for _ in range(subjectTotal):
    subject = list(map(float, input().split()))
    
    result += [subject]

zipped = zip(*result)

for scores in zipped:
    average = (sum(scores) / len(scores))
    print(average)
    
