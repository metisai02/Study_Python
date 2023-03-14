
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]

array = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
      
numbers = int(input("what numbuers do you wanna see? \n"))

col = int(numbers/10)
row = int(numbers%10)
23

array[col -1][row-1] = 'X'

print(col)
print(row)
print(f"{row1}\n{row2}\n{row3}")