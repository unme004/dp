def solve_sudoku(board):
	def empty_cell():
		return next(((row, col) for row in range(9) for col in range(9) if board[row][col]==0), None)

	def valid(row, col, num):
		box_row, box_col = row//3*3, col//3*3
		return not any(
			board[row][i]==num or board[i][col]==num or
			board[box_row+i//3][box_col+i%3]==num for i in range(9)
		)

	def solve():
		cell = empty_cell()
		if not cell: return True
		row, col = cell
		for num in range(1,10):
			if valid(row,col,num):
				board[row][col]=num
				if solve(): return True
				board[row][col]=0
		return False

	solve()
	for row in board: print(*row)

board = [list(map(int, input().split())) for _ in range(9)]

solve_sudoku(board)
