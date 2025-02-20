line1 = input().split()
line2 = input().split()
line3 = input().split()

winner = ""

if line1[0] == line1[1] == line1[2] == '1' or line1[0] == line1[1] == line1[2] == '2':
    if line1[0] == '1':
        winner = "First"
    else:
        winner = "Second"

elif line2[0] == line2[1] == line2[2] == '1' or line2[0] == line2[1] == line2[2] == '2':
    if line2[0] == '1':
        winner = "First"
    else:
        winner = "Second"

elif line3[0] == line3[1] == line3[2] == '1' or line3[0] == line3[1] == line3[2] == '2':
    if line3[0] == '1':
        winner = "First"
    else:
        winner = "Second"

elif line1[0] == line2[0] == line3[0] == '1' or line1[0] == line2[0] == line3[0] == '2':
    if line1[0] == '1':
        winner = "First"
    else:
        winner = "Second"

elif line1[1] == line2[1] == line3[1] == '1' or line1[1] == line2[1] == line3[1] == '2':
    if line1[1] == '1':
        winner = "First"
    else:
        winner = "Second"

elif line1[2] == line2[2] == line3[2] == '1' or line1[2] == line2[2] == line3[2] == '2':
    if line1[2] == '1':
        winner = "First"
    else:
        winner = "Second"

elif line1[0] == line2[1] == line3[2] == '1' or line1[0] == line2[1] == line3[2] == '2':
    if line1[0] == '1':
        winner = "First"
    else:
        winner = "Second"

elif line1[2] == line2[1] == line3[0] == '1' or line1[2] == line2[1] == line3[0] == '2':
    if line1[2] == '1':
        winner = "First"
    else:
        winner = "Second"

if winner != "":
    print(f"{winner} player won")
else:
    print("Draw!")
