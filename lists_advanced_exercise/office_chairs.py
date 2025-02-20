number_of_rooms = int(input())

total_chairs = 0

for room in range(1, number_of_rooms + 1):
    chairs, visitors = input().split()
    difference = len(chairs) - int(visitors)
    if difference < 0:
        print(f"{abs(difference)} more chairs needed in room {room}")
    total_chairs += difference

if total_chairs >= 0:
    print(f"Game On, {total_chairs} free chairs left")