
import sys

#PLAYER PIECES (Or winner if interpreted as game result)
P1='O'
P2='X'

#GAME RESULTS
TIE='T'
UNDECIDED='?'

class GameState:
	def __init__(self,x,y):
		#hiding GameState representation to avoid locking into a row/column bias
		self._board = [['']*8]*8
	def get(self,x,y):
		return self.board[x][y]
	def _set(self,x,y,val):
		self._board[x][y] = val
	#array of strings to array of array of chars
	def aos2aoaoc(aos):
		aoaoc = []
		for str in aos:
			aoc = []
			for c in str:
				aoc.append(c)
			aoaoc.append(aoc)
		return aoaoc

	def dirs():
		return [(1,0),(0,1),(1,1)]
	def winner(self):
		empties = 0
		x = 0
		for row in self._board:
			y = 0
			for c in row:
				if c == '-':
					empties+=1
					y+=1
					continue

				for dir in GameState.dirs():
					i=1
					while i<4:
						if c==self._board[x+i*dir[0]][y+i*dir[1]]:
							i+=1
							continue
						else:
							break
					if i==4:
						return c
					else:
						continue
				y+=1
			x+=1

		if empties ==0:
			return TIE

		return UNDECIDED

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

	b1 = GameState(8,8)
	b2 = GameState(8,8)
	b1._board = GameState.aos2aoaoc(testcase1)
	b2._board = GameState.aos2aoaoc(testcase2)
	assert b1.winner() == 'O'
	assert b2.winner() == 'O'


if len(sys.argv) >1 and sys.argv[1]=="test":
	test()
