global N
N=4   
def isSafe(board, row, col):
	if any(board[row][i] == 1 for i in range(col)):
		return False
	if any(board[i][j] == 1 for i, j in zip(range(row, -1, -1), range(col, -1, -1))):
		return False
	if any(board[i][j] == 1 for i, j in zip(range(row, N, 1), range(col, -1, -1))):
		return False
	return True

def solveNQ(board, col):
	if col >= N:
		return True
	for i in range(N):
		if isSafe(board, i, col):
			board[i][col] = 1
			if solveNQ(board, col + 1):
				return True
			board[i][col] = 0
	return False

board = [[0] * N for _ in range(N)]
if solveNQ(board, 0):
    for row in board:
    	print(row)
