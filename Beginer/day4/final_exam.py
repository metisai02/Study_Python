
import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

    # Code that might raise an exception
my_list = [rock, paper, scissors]
number = int(input("what do you choose? type 0 for rock, type 1 for paper and type 2 for scissors.\n"))
users = my_list[number]
computer  = random.choice(my_list)
print(f"you choice:\n{users}")
print(f"computer choice:\n{computer}")

if users == computer:
    print("draw")
elif users == rock and computer == paper:
    print("lose")
elif users == rock and computer == scissors:
    print("win")
elif users == paper and computer == rock:
    print("win")
elif users == paper and computer == scissors:
    print("lose")
elif users == scissors and computer == paper:
    print("win")
else:
    print("lose") 

