
age = input("What is your current age? ")

n_age = int(age)
yrs_left = 90 - n_age
#print(yrs_left)
days_left = yrs_left * 365
#print(days_left)
wks_left = yrs_left * 52
#print(wks_left)
mths_left = yrs_left * 12
#print(mths_left)
print(f"You have {days_left} days, {wks_left} weeks, and {mths_left} months left.")