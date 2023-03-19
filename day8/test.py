

str = "hello"
list_1 = list(str.strip("")) #convert string to list
list_1[0] = 'c'
str = ''.join(list_1) #convert list to string
print(list_1)
print(str)