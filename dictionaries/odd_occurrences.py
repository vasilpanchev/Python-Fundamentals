words = input().split()
occurrences = {}

for word in words:
    word = word.lower()
    if word not in occurrences:
        occurrences[word] = 1
    else:
        occurrences[word] += 1

for (key, value) in occurrences.items():
    if value % 2 == 1:
        print(key, end=" ")
