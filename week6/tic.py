board = [ ["X", "O", "#"],
          ["X", "X", "X"],
          ["#", "#", "#"] ]


def board_to_string(board):
	st = ''
	counter = 0
	for i in board:
		st += '| '
		st += ' | '.join(i) 
		st += ' |'
		st += '\n'
	return st


print(board_to_string(board))
# print("X|O|#\nX|X|X\n#|#|#")


