
#from replit import clear
import os

diractory = {}
end_game = False

def max_in_dic():
    max = 0
    name = ''
    for char in diractory:
        if diractory[char] > max:
            max = diractory[char]
            name = char
    print(f"chuc mung a {name} co muc gia {max}")

while(not end_game):
    name = input("whats ur name?: ")
    bid = int(input("whats ur bid:$ "))
    diractory[name] = bid
    
    state = input("Are they any other bidder?:'yes' or 'no ")
    if state == 'no':
        end_game = True
    os.system('cls')

max_in_dic()
