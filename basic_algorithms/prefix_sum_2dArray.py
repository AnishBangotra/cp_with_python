# Prefix Sum of Matrix/2D array

# A matrix (or 2D array) data[][] of integers you have, finding prefix sum matrix for it.
# prefix sum matrix be pref[][]. The value of pref[i][j] contains sum of all values which are above it or on left of it.

data = [[1,3,5,7],
		[1,3,5,7],
		[1,3,5,7],
		[1,3,5,7]]

row, col =4,4
#creating prefix sum matrix
pref = [[0 for x in range(col)] for y in range(row)]
#storing first element
pref[0][0] = data[0][0]
#updating columns and rows
for i in range(1,col):
	pref[0][i] = pref[0][i-1] + data[0][i]

for i in range(row):
	pref[i][0] = pref[i-1][0] + data[i][0]
#Applying formula
for i in range(1, row):
	for j in range(1, col):
		pref[i][j] = (pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1] + data[i][j])

for i in range(row):
	for j in range(col):
		print(pref[i][j], end=" ")
	print()
