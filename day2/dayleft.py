
age = input("how old are you? ")

month_left = (90 - int(age))*12
week_left = (90 - int(age)) * 52
day_left = week_left*7

#print(f) help to print variables without casting to string
print(
    f"you have {day_left} days left, {month_left} months left, {week_left} weeks left")
