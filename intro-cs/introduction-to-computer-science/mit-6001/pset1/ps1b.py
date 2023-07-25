# user inputs
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))

portion_down_payment = 0.25
current_savings = 0
r = 0.04
months = 0

while current_savings < total_cost * portion_down_payment:
    monthly_savings = (annual_salary / 12) * portion_saved
    current_savings += current_savings * r / 12 + monthly_savings
    months += 1
    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise

print("Number of months: " + str(months))