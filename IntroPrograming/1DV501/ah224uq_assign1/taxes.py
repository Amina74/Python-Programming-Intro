income = int(input("Please provide monthly income : "))
if income < 38000:
    tax = income * 0.30
elif income >= 38000 and  income <= 50000:
     tax = (income * 0.30) + ((income - 38000) * 0.05)
    #tax = (income * 0.35)
elif income > 50000:
    tax = (income * 0.30) + ((income - 38000) * 0.05) + ((income - 50000) * 0.05)
print("Corresponding income tax :", int(tax))