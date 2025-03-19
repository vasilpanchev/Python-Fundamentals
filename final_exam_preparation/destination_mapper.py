import re

places = input()
pattern = r"(=|/)([A-Z][A-Za-z]{2,})\1"
locations = re.finditer(pattern, places)

destinations = []
travel_points = 0

for location in locations:
    destinations.append(location.group(2))
    points = len(location.group(2))
    travel_points+=points

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")
