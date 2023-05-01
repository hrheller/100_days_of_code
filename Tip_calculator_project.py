print("Welcome to the Tip Calculator")
bill = input("What was the total bill? $")
tip = input("What percentage of tip would you like to give? 10, 12, 15? ")
people = input("How many people to split the bill? ")
split_bill = (float(bill) / int(people)) * (float(tip) / 100 + 1)
#x = round(split_bill, 2)
#formating to 2 decimal places
x = "{:.2f}".format(split_bill)
print(f"Each person should pay: ${x}")