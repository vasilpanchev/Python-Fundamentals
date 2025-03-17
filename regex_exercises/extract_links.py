import re

text = input()
pattern = r"www\.[a-zA-Z\d\-]+(\.[a-z]+)+\b"
while text:
    links = re.finditer(pattern, text)
    for link in links:
        print(link.group())
    text = input()