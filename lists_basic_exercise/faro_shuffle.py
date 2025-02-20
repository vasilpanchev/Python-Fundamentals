def shuffle(deck):
    a = []
    b = []

    for i in range(0, int(len(deck) / 2)):
        a.append(deck[i])

    for i in range(int(len(deck) / 2), len(deck)):
        b.append(deck[i])

    mixed_deck = []
    for i in range(len(a)):
        mixed_deck.append(a[i])
        mixed_deck.append(b[i])
    return mixed_deck


deck_of_cards = input().split(' ')
shuffles = int(input())

for _ in range(shuffles):
    deck_of_cards = shuffle(deck_of_cards)

print(deck_of_cards)
