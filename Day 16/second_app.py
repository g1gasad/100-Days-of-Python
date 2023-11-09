from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Col1", [1,2,3], align='l')
table.add_column("Col2", ['a', 'b', 'c'], align='r')

print(table)
