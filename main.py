bill_cost = float(input("What was the bill cost in dollars?\n"))
people_num = int(input("How many people do you split the bill between?\n"))
tip_percent = float(input("What tip percentage do you want to give?\n"))

fair_pay = round(round(bill_cost / people_num, 2) * (1+ 0.01 * tip_percent), 2)

print(f"Each person has to pay {fair_pay}")