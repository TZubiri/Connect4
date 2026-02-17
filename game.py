
import sys

#PLAYER PIECES (Or winner if interpreted as game result)
P1='O'
P2='X'

#GAME RESULTS
TIE='T'
UNDECIDED='?'

LINE=4 #CONNECT FOUR

class GameState:
	def __init__(self,x,y):
		#hiding GameState representation to avoid locking into a row/column bias
		self._board = [['-']*x for i in range(y)]
	def get(self,x,y):
		return self._board[x][y]
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
	def printable_board(self):
		str = ""
		for row in self._board:
			for c in row:
				str+=c
			str+='\n'
		return str

	def firstfree(self,col):
		i=7
		while i>=0:
			if self.get(i,col)== '-':
				return i
			i-=1
		return None
	def play(self,col,player):
		ff  = self.firstfree(col)
		if ff is None:
			raise Exception("Can't play column " + str(col) + " . Column is full")
		self._set(ff,col,player)

	def dirs():
		return [(1,0),(0,1),(1,1),(-1,1)]
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
					while i<LINE:
						checking_x = x+ i*dir[0]
						checking_y = y+ i*dir[1]
						if checking_x<0 or checking_y <0 or checking_x>7 or checking_y>7:
							break #not a win (avoid OOB)
						if c==self._board[checking_x][checking_y]:
							i+=1
							continue #maybe a win
						else:
							break # not a win
					if i==LINE:
						return c #definitely a win
					else:
						continue #try another direction
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
	testcase3= [
			'--------',
			'--------',
			'--------',
			'--------',
			'--OOXO--',
			'--OXOXO-',
			'-XXOXOX-',
			'-XOOOXX-',
]

	b1 = GameState(8,8)
	b2 = GameState(8,8)
	b3 = GameState(8,8)
	b1._board = GameState.aos2aoaoc(testcase1)
	b2._board = GameState.aos2aoaoc(testcase2)
	b3._board = GameState.aos2aoaoc(testcase3)
	assert b1.winner() == 'O'
	assert b2.winner() == 'O'
	assert b3.winner() == 'X'


if len(sys.argv) >1 and sys.argv[1]=="test":
	test()
if __name__ == "__main__" or (len(sys.argv) > 1  and sys.argv[1] == "main"):
	import random
	gs = GameState(8,8)
	def eval(gs):
		win = gs.winner()
		if win=='?':
			return
		print("\n\n")
		print(gs.printable_board())
		if win=='T':
			print("\n\nTHE GAME IS A TIE!")
			exit()
		if win=='O':
			print("\n\nPLAYER WINS!")
			exit()
		if win=='T':
			print("\n\nPLAYER LOSES!")
			exit()
	while True:
		print(gs.printable_board())
		move = input("Select the a column from 1-8\n")
		move = int(move)
		if move<1 or move>8:
			raise Exception("Column not in 1-8 range")
		gs.play(move-1,'O')
		eval(gs)

		opp_move = random.randrange(0,8)
		gs.play(opp_move,'X')
		print('opponent plays column '+ str(opp_move))
		eval(gs)
