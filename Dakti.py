n = int(input())

for _ in range(n):
    value = input().split()

    sorted_strings = sorted(value, key=lambda x: int(
        ''.join(text for text in x if text.isdigit())))
    words = ["".join([char for char in word if not char.isdigit()])
             for word in sorted_strings]

    print(" ".join(words))
