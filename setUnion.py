num_english = int(input())
eng_subs = set(map(int, input().split()))

num_french = int(input())
french_subs = set(map(int, input().split()))

total_students = eng_subs.union(french_subs)

print(len(total_students))
