word = input()
unique_characters = set(word)

if len(unique_characters) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
    
# time complexity: O(1)
# space complexity: O(n)
