import random
import os

card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



end_game = False
take = True


def calculate(list):
    rezult = 0
    rezult = sum(list)
    if sum(list) == 21 and len(list) == 2:
        return 0
    if 11 in list and rezult > 21:
        rezult = rezult - 10
    return rezult


def compare(player, computer):
    r_play = calculate(player)
    r_com = calculate(computer)
    if r_play > 21 and r_com > 21:
        return "You lose"
    elif r_play == r_com:
        return "Draw"
    elif r_play == 0:
        return "may mai dinh"
    elif r_play == 0:
        return "may la sieu nhan"
    elif r_play > 21:
        return "you loose"
    elif r_com > 21:
        return "you win"
    elif r_play > r_com:
        return "you win"
    else:
        return "you loose"


while not end_game == True:
    player = []
    computer = []
    for count in range(2):
        player.append(random.choice(card_list))
        computer.append(random.choice(card_list))
    print(f"your card: {player}")
    print(f"computer's first card: {computer[0]}")
    while take == True:
        state = input("Type 'y' to get another card, type 'n' to pass: ")
        if state == 'y':
            player.append(random.choice(card_list))
            if calculate(player) > 21:
                take = False
        else:
            take = False
    print(companre(player, computer))
    take = True
    os.system('cls')
