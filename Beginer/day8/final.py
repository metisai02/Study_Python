alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
end = False

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    text_list = list(text.strip(""))
    cipher_text = []
    for char in text_list:
        if char in alphabet:
            cipher_text.append(alphabet[text_list.index(char)+shift])
    print(''.join(cipher_text))
def decrypt(text, shift):
    text_list = list(text.strip(""))
    plain_text = []
    for char in text_list:
        if char in alphabet:
            plain_text.append(alphabet[text_list.index(char)-shift])
    print(''.join(plain_text))

def create(direction, text, shift):
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Invalid input")

while end == False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))    
    create(direction, text, shift)
    condittion = input("do you want to end this message: yes or no?\n")
    if condittion == "yes":
        end = True

        
        
    

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 