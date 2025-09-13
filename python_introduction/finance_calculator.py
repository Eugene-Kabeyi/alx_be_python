income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your monthly expenses: "))
savings = income - expenses
yearly_savings = savings * 12 + (savings * 12 * 0.05)  # Savings for 5% annual interest
print(f"Your monthly savings are: ${int(savings)}.")
print(f"Projected savings after one year, with interest, is: ${int(yearly_savings)}.")