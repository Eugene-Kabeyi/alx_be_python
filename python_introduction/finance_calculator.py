monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
yearly_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)  # Savings for 5% annual interest
print(f"Your monthly savings are: ${int(monthly_savings)}.")
print(f"Projected savings after one year, with interest, is: ${int(yearly_savings)}.")