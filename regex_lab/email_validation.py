import re
pattern = r"\b[a-z0-9]+@[a-z0-9]+\.[a-z\.]+\b"
txt = input()
matches = re.findall(pattern,txt)