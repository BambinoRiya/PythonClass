number_of_words = int(input())
words = []

for i in range(number_of_words):
    word = input()
    words.append(word)


for word in words:
    split_index = 2  # Index at which the split occurs

    first_part = word[:split_index]  # Extract the first part before the split

    # Concatenate the parts with '... ' and add a question mark
    result = first_part + '... ' + word + '?'

    print(result)
