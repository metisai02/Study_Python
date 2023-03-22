import random


def hard_level():
    return 5


def easy_level():
    return 10


def check(number, rezult):
    if number == rezult:
        return 0
    elif number > rezult:
        return 'too hight'
    else:
        return 'too low'


end = False
count = 0
print("welcom to play game")
print("im thinking of a number between 1 to 100")
level = input("hard or easy")
if level == 'hard':
    count = hard_level()
else:
    count = easy_level()
rezult = random.randint(0, 100)
while not count == 0:
    number = int(input("make a guess: "))
    if check(number, rezult) == 0:
        print("ur are conrect")
        count = 0
    else:
        print(check(number, rezult))
        count -= 1
        print(f"count: {count}")
        if count == 0:
            print("you loose")
