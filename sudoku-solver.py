# %%
# initializing placeholder puzzle array[array]
puzzle = [[0 for x in range(9)] for y in range(9)]

# %%
# printing filled grid
def print_grid(p):
	"""prints a filled grid using the grid provided

	Args:
		p ([[int]]): puzzle grid with 0's for empty cells

	Returns:
		int: 0
	"""
	print("-" * (19 * 2 + 1))
	for i in range(9):
		for j in range(9):
			print(" | " + str(p[i][j]), end="")
		print(' |')
		print("-" * (19 * 2 + 1))
	return 0

# %%
def is_valid(grid, row, col, num):
	"""checks sudoku grid for numbers in invalid positions

	Args:
		grid ([[[int]]]): list of lists of lists of ints
		row ([[int]]): a list of horizontal rows
		col ([int]): the horizontal position of ints
		num (int): the number to check against

	Returns:
		bool: Validity of sudoku grid
	"""
	for x in range(9):
		if grid[row][x] is num:
			return False
	for x in range(9):
		if grid[x][col] is num:
			return False
	start_row = row - row % 3
	start_column = col - col % 3
	for i in range(3):
		for j in range(3):
			if grid[i + start_row][j + start_column] is num:
				return False
	return True

# %%
def solve_sudoku(grid, row, col):
	"""solves grid populated with helper digits

	Args:
		grid ([[int]]): sudoku grid populated with helpers
		row (int): initial row number
		col (int): initial column number

	Returns:
		bool: recursively calls the function to check each row for the appropriate entry, then fills it
	"""
	if row is 8 and col is 9:
		return True

	if col is 9:
		row += 1
		col = 0

	if grid[row][col] > 0:
		return solve_sudoku(grid, row, col + 1)

	for num in range(1, 10):
		if is_valid(grid, row, col, num):
			grid[row][col] = num

			if solve_sudoku(grid, row, col + 1):
				return True
		grid[row][col] = 0
	return False

# %%
# Driving Code

# populating empty grid with helpers, row by row
# row 1
puzzle[0] = [0, 0, 0, 1, 2, 3, 0, 0, 0]

# row 2
puzzle[1] = [0, 0, 0, 0, 0, 0, 7, 0, 0]

# row 3
puzzle[2] = [0, 0, 8, 0, 0, 0, 0, 1, 0]

# row 4
puzzle[3] = [0, 0, 0, 0, 7, 0, 5, 6, 0]

# row 5
puzzle[4] = [0, 6, 0, 0, 0, 0, 0, 4, 2]

# row 6
puzzle[5] = [0, 2, 0, 0, 0, 8, 0, 0, 0]

# row 7
puzzle[6] = [4, 3, 0, 0, 0, 0, 0, 0, 6]

# row 8
puzzle[7] = [0, 0, 6, 0, 9, 0, 8, 0, 0]

# row 9
puzzle[8] = [0, 0, 0, 0, 0, 5, 0, 0, 3]

print_grid(puzzle)

# %%
if solve_sudoku(puzzle, 0, 0):
	print_grid(puzzle)
else:
	print("no solution")
