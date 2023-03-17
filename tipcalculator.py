print("Welcome to Tip Calculator")
total_bill=float(input("What was the total bill? $"))
tip=int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people=int(input("How many people to split the bill? "))
bill_tip= (total_bill/100) * (tip+100)
pay= bill_tip/people
print(f"Each person shoul pay: ${round(pay,2)}")