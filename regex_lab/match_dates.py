import re

pattern = r"\d{1,2}-[A-Z][a-z]{2}-\d{4}"
text = "I am born on 30-Dec-1994. My father is born on the 9-Jul-1955. 01-July-2000 is not a valid date."

matches = re.findall(pattern, text)

print(matches)