synonyms = {}
n = int(input())
for i in range(n):
    word = input()
    synonym = input()
    if word in synonyms.keys():
        synonyms[word].append(synonym)
    else:
        synonyms[word] = [synonym]

for (word, synonym) in synonyms.items():
    print(f"{word} - {', '.join(synonyms[word])}")
