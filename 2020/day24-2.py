import copy

class HexBoard:
	def __init__(self, boardSize = 100):
		self.board = {}

		for i in range(-boardSize, boardSize):
			self.board[i] = {}
			for j in range(-boardSize, boardSize):
				self.board[i][j] = {}
				for k in range(-boardSize, boardSize):
					if i + j + k == 0:
						self.board[i][j][k] = None

	def add_tile(self, pos):
		self.board[pos[0]][pos[1]][pos[2]] = HexTile(pos)

	def toggle_tile_color(self, pos):
		self.board[pos[0]][pos[1]][pos[2]].toggle_color()

	def count_black_tiles(self):
		count = 0
		for i in self.board:
			for j in self.board[i]:
				for k in self.board[i][j]:
					if self.board[i][j][k] and self.board[i][j][k].isBlack:
						count += 1
		return count

	def make_adj_tiles(self):
		boardCopy = copy.deepcopy(self.board)
		for i in self.board:
			for j in self.board[i]:
				for k in self.board[i][j]:
					if self.board[i][j][k] and self.board[i][j][k].isBlack:
						boardCopy = self.make_adj(boardCopy, [i, j, k])
		self.board = boardCopy

	def make_adj(self, board, pos):
		for ai in [1,0,-1]:
			for aj in [1,0,-1]:
				for ak in [1,0,-1]:
					if ai == 0 and aj == 0 and ak == 0:
						continue
					di = pos[0] + ai
					dj = pos[1] + aj
					dk = pos[2] + ak
					if not di in board or not dj in board[di] or not dk in board[di][dj]:
						continue
					if not board[di][dj][dk]:
						board[di][dj][dk] = HexTile([di, dj, dk])
		return board

	def cycle(self):
		self.make_adj_tiles()
		toFlip = []
		for i in self.board:
			for j in self.board[i]:
				for k in self.board[i][j]:
					if self.board[i][j][k]:
						if self.board[i][j][k].check_flip(self.board):
							toFlip.append([i,j,k])
		for i,j,k in toFlip:
			self.board[i][j][k].toggle_color()

class HexTile:
	def __init__(self, pos):
		self.pos = pos
		self.isBlack = False

	def toggle_color(self):
		self.isBlack = not self.isBlack

	def count_adj_black(self, board):
		count = 0
		for ai in [1,0,-1]:
			for aj in [1,0,-1]:
				for ak in [1,0,-1]:
					if ai == 0 and aj == 0 and ak == 0:
						continue
					di = self.pos[0] + ai
					dj = self.pos[1] + aj
					dk = self.pos[2] + ak
					if not di in board or not dj in board[di] or not dk in board[di][dj]:
						continue
					if board[di][dj][dk] and board[di][dj][dk].isBlack:
						count += 1
		return count

	def check_flip(self, board):
		adjBlack = self.count_adj_black(board)
		if self.isBlack:
			if adjBlack == 0 or adjBlack > 2:
				return True
		else:
			if adjBlack == 2:
				return True
		return False

inFile = open("day24.in", "r").read().split("\n")
inFile.pop()

allTiles = {}

board = HexBoard()

for order in inFile:
	pos = [0, 0, 0]

	i = 0
	while i < len(order):
		direction = order[i]
		if not direction in ['e','w']:
			direction += order[i + 1]
			i += 1

		if direction == 'ne':
			pos[0] += 1
			pos[2] -= 1
		elif direction == 'sw':
			pos[0] -= 1
			pos[2] += 1
		elif direction == 'e':
			pos[0] += 1
			pos[1] -= 1
		elif direction == 'w':
			pos[0] -= 1
			pos[1] += 1
		elif direction == 'se':
			pos[1] -= 1
			pos[2] += 1
		elif direction == 'nw':
			pos[1] += 1
			pos[2] -= 1
		i += 1

	if not board.board[pos[0]][pos[1]][pos[2]]:
		board.add_tile(pos)

	board.toggle_tile_color(pos)

for i in range(100):
	board.cycle()

print(board.count_black_tiles())
