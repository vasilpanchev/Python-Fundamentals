import re
bought_furniture = []
total_money_spent =0
line=input()
pattern = r">>([a-zA-Z]+)<<(\d+\.*\d+)\!(\d+)\b"
while line!="Purchase":
    purchase = re.finditer(pattern,line)
    for detail in purchase:
        furniture = detail.group(1)
        price = float(detail.group(2))
        quantity = int(detail.group(3))
        bought_furniture.append(furniture)
        total_money_spent+=price*quantity
    line = input()

print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_money_spent:.2f}")