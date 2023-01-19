annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))

portion_down_payment = total_cost * 0.25
current_savings = 0
months = 0
r = 0.04

monthly_salary = annual_salary / 12
monthly_r = r / 12
monthly_portion = monthly_salary * portion_saved

while current_savings < portion_down_payment:
    monthly_interest = current_savings * monthly_r
    current_savings += monthly_interest + monthly_portion
    months += 1
    if months % 6 == 0:
        monthly_salary += monthly_salary * semi_annual_raise
        monthly_portion = monthly_salary * portion_saved

print("Number of months:", months)