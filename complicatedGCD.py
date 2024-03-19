def complicatedGCD(a,b):
    if b == a:
        return b
    else:
        return 1

a,b = map(int,input().split())
print(complicatedGCD(a,b))
