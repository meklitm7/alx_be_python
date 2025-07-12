# Welcome and Income Input
username = input("What's your name?: ")
print(f"Welcome to {username}'s Budget Manager!")
salary = float(input("What's your monthly income (salary)?: "))
business = float(input("What's your monthly business income?: "))
total_income = salary + business
print(f"Total Monthly Income: ${total_income:.2f}")

# Expenses and Savings Calculation
transport = float(input("What's your transportation expenses for the month?: "))
food = float(input("Food expenses for the month?: "))
total_expenses = transport + food
print(f"Total Expenses for the Month: ${total_expenses:.2f}")

monthly_savings = total_income - total_expenses
print(f"Total Monthly Savings: ${monthly_savings:.2f}")