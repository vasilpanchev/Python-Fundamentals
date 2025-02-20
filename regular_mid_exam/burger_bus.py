number_of_cities = int(input())
total_income = 0
total_expenses = 0
for city in range(1, number_of_cities + 1):
    name_of_city = input()
    earned_money = float(input())
    expenses = float(input())
    if city % 5 == 0:
        earned_money -= 0.10 * earned_money
    elif city % 3 == 0:
        expenses += 0.50 * expenses
    total_income += earned_money
    total_expenses += expenses
    profit_for_city = earned_money - expenses
    print(f"In {name_of_city} Burger Bus earned {profit_for_city:.2f} leva.")

total_profit = total_income - total_expenses
print(f"Burger Bus total profit: {total_profit:.2f} leva.")
