total_cost = 1000000
semi_annual_raise = 0.07
r = 0.04
epsilon = 100
low = 0
high = 10000
portion_down_payment = total_cost * 0.25
steps = 1

annual_salary = int(input("Enter the starting salary: "))

while high - low > 1:
    current_savings = 0
    months = 0
    monthly_salary = annual_salary / 12
    portion_saved = ((high+low) // 2) / 10000
    monthly_portion = monthly_salary * portion_saved
    while months < 36:
        monthly_interest = current_savings * (r/12)
        current_savings += monthly_interest + monthly_portion
        months += 1
        if months % 6 == 0:
            monthly_salary += monthly_salary*semi_annual_raise
            monthly_portion = monthly_salary * portion_saved

    if abs(current_savings - portion_down_payment) < epsilon:
        break

    guess = int(portion_saved * 10000)
    if current_savings < portion_down_payment:
        low = guess
    else:
        high = guess
    steps += 1

if abs(current_savings - portion_down_payment) < epsilon:
    print("Best saving rate:", portion_saved)
    print("Steps in bisection search:", steps)
else:

    print("It is not possible to pay the down payment in three years.")