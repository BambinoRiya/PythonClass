t = int(input())

for _ in range(t):
    s = input()  # zzaaz
    distinct_chars = set()

    # print(distinct_chars)

    i = 0  # pointer
    while i < len(s):
        # to fix index out of range, to handle the last number
        if i + 1 < len(s) and s[i] == s[i + 1]:
            i += 1
        else:
            distinct_chars.add(s[i])
        i += 1

    sorted_chars = sorted(distinct_chars)
    print(''.join(sorted_chars))
