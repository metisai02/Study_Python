import random
from art import logo
from art import vs
from game_data import data
import os

#hàm này nhặt được từ video
def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess 
    and returns True if they got it right.
    Or False if they got it wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def compare(player1, player2):
    r_1 = player1["follower_count"]
    r_2 = player2["follower_count"]
    if r_1 > r_2:
        return 0
    else:
        return 1


def display(player1, player2):
    print(
        f"compare A: {player1['name']},{player1['description']}, from {player1['country']}")
    print(vs)
    print(
        f"compare B: {player2['name']},{player2['description']}, from {player2['country']}")


player1 = random.choice(data)
player2 = random.choice(data)
score = 0
end_game = False
while not end_game:
    player1 = random.choice(data)
    player2 = random.choice(data)

    while player1['name'] == player2['name']:
        player2 = random.choice(data)

    display(player1, player2)
    choose = input(
        "who has folowers higher than the other side? A or B\n").lower()
    if choose == 'a' and compare(player1, player2) == 0:
        os.system('cls')
        print(logo)
        score += 1
        print("you're right")
        print(f"ur score is: {score}")
    elif choose == 'b' and compare(player1, player2) == 1:
        os.system('cls')
        print(logo)
        score += 1
        print("you're right")
        print(f"ur score is: {score}")
    else:
        os.system('cls')
        print(logo)
        print(f"you lose\nur score is: {score}")
        end_game = True
