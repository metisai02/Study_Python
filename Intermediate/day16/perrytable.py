

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Member",["metisai","Trung","Hanh"])
table.add_column("Type",["noob","pro","pro"])
print(table.align)
table.align = "r"

print(table)