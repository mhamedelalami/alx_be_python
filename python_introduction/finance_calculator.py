income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = income - expenses

projected_savings = monthly_savings * 12 * 1.05

print(f"Your monthly savings are {monthly_savings} "), 
print(f"Projected savings after one year, with interest, is: {projected_savings} ")
