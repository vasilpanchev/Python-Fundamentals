import re

text = input()
word = input()
pattern = r"\b" + f"{word}" + r"\b"

matches = re.findall(pattern, text, re.IGNORECASE)
print(len(matches))
