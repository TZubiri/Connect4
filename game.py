
P1='O'
P2='X'

class GameState:
	def __init__(self,x,y):
		#hiding board representation to avoid locking into a row/column bias
		self._board = [['']*8]*8
	def get(self,x,y):
		return self.board[x][y]
	def _set(self,x,y,val):
		self._board[x][y] = val
	#array of strings to array of array of chars
	def aos2aoaoc(aos):
		aoaoc = []
		for row in aos:
			aoc = []
			for c in row:
				aoc.append(c)
			aoaoc.append(aoc)
		return aoaoc

	def winner(self)
		for 


def test():
	testcase1= [
			'--------',
			'--------',
			'--------',
			'--------',
			'--OOOO--',
			'--OXOXO-',
			'-XXOXOX-',
			'-XXOXOX-',
]
	testcase2= [
			'--------',
			'--------',
			'--------',
			'--------',
			'--OOXO--',
			'--OXOXO-',
			'-XOOXOX-',
			'-XOOXXX-',
]

	b1 = Board(8,8)
	b2 = Board(8,8)
	b1._board = Board.aos2aoaoc(testcase1)
	b2._board = Board.aos2aoaoc(testcase2)
	assert Board.winner() == 'O'
	assert Board.winner() == 'X'

