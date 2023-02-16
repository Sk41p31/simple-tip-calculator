#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill_cost = float(input("What was the bill cost in dollars?\n"))
people_num = int(input("How many people do you split the bill between?\n"))
tip_percent = float(input("What tip percentage do you want to give?\n"))

fair_pay = round(round(bill_cost / people_num, 2) * (1+ 0.01 * tip_percent), 2)

print(f"Each person has to pay {fair_pay}")