
print ("wellcome to the tip calculator\n")
total = input("what was the total bill? ")
precentage = int(input("what percentage tip would you want to give? 10 , 15 , or 20 "))
people = int(input("how many people to split the bill "))

money = (float(total) /people)*(1 + precentage/100)
# round để làm tròn 2 chữ số
#format để đưa nó có 2 chấm sau dấu phẩy , vì khi money bằng 36.3 thì nó không phải 36.30
print ("{:.2f}".format(round(money,2)) ) 


