tableData = [['apples', 'oranges', 'cherries', 'banana'], ['Alice', 'Bob', 'Carol', 'David'], ['dogs', 'cats', 'moose', 'hippopotamous']]

def printTable(table):
	colWidths = [0]*len(table)
	for a in range(len(table)):
		for b in range(len(table[a])):	
			if len(table[a][b]) > colWidths[a]:
					colWidths[a] = len(table[a][b])	

	for x in range(len(table[0])):
		for y in range(len(table)):
			print(table[y][x].rjust(colWidths[y]), end = ' ')
		print()

printTable(tableData)
