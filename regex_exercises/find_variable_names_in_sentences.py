import re

pattern = r"\b_([a-zA-Z0-9]+)\b"
text = input()
variables = re.findall(pattern, text)
print(','.join(variables))