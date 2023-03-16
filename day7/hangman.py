# Step 1
import random
import hangman_art

# word_list = ["aardvark", "baboon", "camel"]

from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

print(logo)
word = random.choice(word_list)

rezult_list = []
w_list = []
for i in word:
    w_list.append(i)
count = len(stages) - 1


for i in range(0, len(word)):
    rezult_list.append("-")

end_game = False

while not end_game:
    guess = input("Guess a letter: ").lower()

    for i in range(0, len(word)):
        if guess == word[i]:
            rezult_list[i] = guess
        # else:
            # print(stages[i])
    print(f"{' '.join(rezult_list)}")  # convert list to string
    if "-" not in rezult_list:
        end_game = True
        print("you win")
    elif guess not in rezult_list:
        print(stages[count])
        count -= 1
        if count < 0:
            end_game = True
print("you lose")
