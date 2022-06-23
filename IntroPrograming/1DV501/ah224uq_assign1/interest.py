initial_savings= int(input("enter your initial amount:"))
interset_rate = int(input("Interest rate (in percentage) : "))
years = 5
 # finding compound interest
total_amount = initial_savings * (pow((1 + interset_rate / 100), years)) 
print("\nThe value of your savings after 5 years is: ", round(total_amount))
