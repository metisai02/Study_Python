import random

names = ["Angela", "Ben", "Jenny", "Michael",
         "Chloe"]  # creates a list of names

length = len(names)

number_order = random.randint(0, length - 1)  # int random number


# print(f"{name[number_order]} is going to buy the meal today!")

print(f"{random.choice(names)} is going to buy the meal today!")#random.choice(names) random from the lists
