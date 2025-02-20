energy = 100
coins = 100

events_as_string = input()
events = events_as_string.split('|')

for i in range(len(events)):
    event, ingredient = events[i].split('-')
    ingredient = int(ingredient)
    if event == "rest":
        current_energy = energy
        energy += ingredient
        if energy > 100:
            energy = 100
        gained = abs(current_energy - energy)
        print(f"You gained {gained} energy.")
        print(f"Current energy: {energy}.")
    elif event == "order":

        if (energy - ingredient) < 0:
            print("You had to rest!")
            energy += 50
            if energy > 100:
                energy = 100

            continue
        energy -= 30
        coins += ingredient
        print(f"You earned {ingredient} coins.")
    else:
        if (coins - ingredient) < 0:
            print(f"Closed! Cannot afford {event}.")
            break
        else:
            coins -= ingredient
            print(f"You bought {event}.")
else:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
