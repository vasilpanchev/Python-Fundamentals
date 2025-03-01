country_names = input().split(", ")
capital_cities = input().split(", ")

country_capitals = dict(zip(country_names, capital_cities))

for (country, capital) in country_capitals.items():
    print(f"{country} -> {capital}")
