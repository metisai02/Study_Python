#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = []
for i in range(0, nr_letters):
    password.append(random.choice(letters))

for i in range (0,nr_letters - (nr_symbols + nr_numbers)):
    password[i] = random.choice(letters)
for i in range(nr_letters - (nr_symbols + nr_numbers),nr_letters - (nr_numbers)):
    password[i] = random.choice(symbols)
for i in range(nr_letters - (nr_numbers),nr_letters):
    password[i] = random.choice(numbers)

password_2 = ''
for char in password:
    password_2 += char

    #join help to conect list to single sring
# password_1 = ''.join(password) 
# print(password_1)
print(password_2)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P\
password_3 = []
for i in range(0, nr_letters):
    password_3.append(random.choice(letters))
for i in range(0,nr_numbers):

    password_3.append(random.choice(numbers))
for i in range(0,nr_symbols):

    password_3.append(random.choice(symbols))
random.shuffle(password)

for char in password_3:
    password_2 += char
print(password_3)
