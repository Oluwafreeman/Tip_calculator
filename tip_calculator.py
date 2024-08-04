print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))

tip = (percentage/100) * total_bill
total_bill += tip
each_person = total_bill/split
each_person_round = "{:.2f}".format(each_person)
print(f"Each person should pay: ${each_person_round}")

