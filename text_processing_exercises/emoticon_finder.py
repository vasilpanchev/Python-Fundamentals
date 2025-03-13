line = input()

while ":" in line:
    dots_index = line.find(":")
    emoticon = line[dots_index:dots_index + 2]
    print(emoticon)
    line = line.replace(":", "", 1)
