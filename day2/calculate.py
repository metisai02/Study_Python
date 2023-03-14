
weight = input("weight: ")
high = input("high: ")

print(f"Your height is" + str(high) +
      " cm and your weight is " + str(weight) + "kg.")

rezults = float(weight) / (float(high)**2)
print(int(rezults))
