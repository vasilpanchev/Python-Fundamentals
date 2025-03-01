resources = {}
command = input()
while command != "stop":
    resource = command
    quantity = int(input())
    if resource not in resources:
        resources[resource] = 0
    resources[resource] += quantity
    command = input()

for (resource, quantity) in resources.items():
    print(f"{resource} -> {quantity}")
