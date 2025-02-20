deck_of_cards = input().split(', ')
n = int(input())

for i in range(n):
    command = input().split(', ')
    if command[0] == "Add":
        card_name = command[1]
        if card_name not in deck_of_cards:
            deck_of_cards.append(card_name)
            print("Card successfully added")
        else:
            print("Card is already in the deck")

    elif command[0] == "Remove":
        card_name = command[1]
        if card_name in deck_of_cards:
            deck_of_cards.remove(card_name)
            print("Card successfully removed")
        else:
            print("Card not found")

    elif command[0] == "Remove At":
        index = int(command[1])
        if index in range(len(deck_of_cards)):
            deck_of_cards.pop(index)
            print("Card successfully removed")
        else:
            print("Index out of range")

    elif command[0] == "Insert":
        index = int(command[1])
        card_name = command[2]
        if index in range(len(deck_of_cards)):
            if card_name not in deck_of_cards:
                deck_of_cards.insert(index, card_name)
                print("Card successfully added")
            else:
                print("Card is already added")
        else:
            print("Index out of range")

print(', '.join(deck_of_cards))