days_of_pirating = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

plunder = 0

for day in range(1, days_of_pirating + 1):
    plunder += daily_plunder
    if day % 3 == 0:
        plunder += 0.5 * daily_plunder
    if day % 5 == 0:
        plunder -= 0.3 * plunder

if plunder >= expected_plunder:
    print(f"Ahoy! {plunder:.2f} plunder gained.")
else:
    plunder_percentage = plunder / expected_plunder * 100
    print(f"Collected only {plunder_percentage:.2f}% of the plunder.")
