import re
import math
import copy
#import numpy

ROTATE_RIGHT = 1
ROTATE_LEFT = -1

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

DIR_ENUM = ["U", "R", "D", "L"]
FLIPPED_ENUM = ["I", "U"]

WIDTH = 12
LENGTH = 12
# tiles[LENGTH][WIDTH]

def easyMod(val, modVal = 4):
	return val % modVal

class TileBoard:
	def __init__(self, width, length, tiles):
		self.width = width
		self.length = length
		self.tiles = tiles
		self.board = []
		for l in range(length):
			newRow = []
			for w in range(width):
				newRow.append(None)
			self.board.append(newRow)

		self.tileIDs = {}

		startTile = None
		for tile in self.tiles:
			self.tileIDs[tile.tileID] = tile
			tile.set_possible(self.tiles)
			if tile.isCorner:
				startTile = tile

		if startTile == None:
			raise "No corner tile found"

		if startTile.neighbors[0] == None and startTile.neighbors[1] == None:
			startTile.rotate_tile(ROTATE_LEFT)

		elif startTile.neighbors[1] == None and startTile.neighbors[2] == None:
			startTile.rotate_tile(ROTATE_RIGHT)
			startTile.rotate_tile(ROTATE_RIGHT)

		elif startTile.neighbors[2] == None and startTile.neighbors[3] == None:
			startTile.rotate_tile(ROTATE_RIGHT)

		#startTile.direction = 3
		#startTile.flipH = 1

		#self.board[0][0] = startTile
		#self.print_board(self.board)
		#startTile.rotate_tile(ROTATE_RIGHT)
		#startTile.rotate_tile(ROTATE_RIGHT)
		#startTile.flipH = 1

		#self.board[0][1] = self.tileIDs["2311"]
		#self.board[0][2] = self.tileIDs["3079"]
		#self.board[1][0] = self.tileIDs["2729"]
		#self.board[1][1] = self.tileIDs["1427"]
		#self.board[1][2] = self.tileIDs["2473"]
		#self.board[2][0] = self.tileIDs["2971"]
		#self.board[2][1] = self.tileIDs["1489"]
		#self.board[2][2] = self.tileIDs["1171"]

		self.fill_board(startTile, copy.deepcopy(self.board))

	def is_board_valid(self, board):
		for row in board:
			for tile in row:
				if tile:
					pass
					#print(tile)

	def is_board_full(self, board):
		for row in board:
			for tile in row:
				if not tile:
					return False
		return True

	def check_tile_edges(self, tile, pos):
		noneCount = tile.neighbors.count(None)
		if noneCount == 2:
			if not (pos[0] in [0, self.width - 1] and pos[1] in [0, self.width - 1]):
				return False
		elif noneCount == 1:
			if not (pos[0] in [0, self.width - 1] or pos[1] in [0, self.width - 1]):
				return False
			pass
		return True

	def fill_board(self, tile, mockBoard, used = [], pos = [0, 0], debug = True):
		if tile.tileID in used:
			return

		newUsed = copy.deepcopy(used)
		newUsed.append(tile.tileID)
		newBoard = copy.deepcopy(mockBoard)
		newBoard[pos[0]][pos[1]] = tile
		self.print_board(newBoard)

		if debug:
			self.print_board(newBoard)

		if self.is_board_full(newBoard):
			self.board = newBoard

		for dir in [0,1,2,3]:
			relDir = tile.get_rel_dir(dir)

			dX = copy.deepcopy(pos[0])
			dY = copy.deepcopy(pos[1])
			if dir == 0:
				dX -= 1
			elif dir == 1:
				dY += 1
			elif dir == 2:
				dX += 1
			elif dir == 3:
				dY -= 1

			if dX < 0 or dY < 0:
				continue
			if dX >= self.length or dY >= self.width:
				continue
			if not newBoard[dX][dY] == None:
				continue

			for n in tile.possibleNeighbors[relDir]:
				nextTile = self.tileIDs[n]
				if not self.check_tile_edges(nextTile, [dX, dY]):
					continue
				nTiles = nextTile.find_edge(tile.get_edge(relDir))
				for tiles in nTiles:

					#print(nTiles)

					tileEdge = tile.get_edge(relDir)
					nextTile.flipV = 1
					nextEdge = nextTile.get_edge(relDir)
					#print(tileEdge)
					#print(nextEdge)

					nextTile.orient_tile(dir, tileEdge)

					#nextTile.direction = easyMod(dir + 2) - tiles[0]
					#if nextTile.direction < 0:
					#	nextTile.direction = 4 + nextTile.direction

					#if dir in [0,2]:
					#	print("H", tile.flipH)
					#	if tile.flipH == 0:
					#		nextTile.flipH = tiles[1]
					#	else:
					#		nextTile.flipH = abs(tiles[1] - 1)
					#elif dir in [1,3]:
					#	print("V", tile.flipV)
					#	if tile.flipV == 0:
					#		nextTile.flipV = tiles[1]
					#	else:
					#		nextTile.flipV = abs(tiles[1] - 1)

					if debug:
						input()

					self.fill_board(nextTile, newBoard, newUsed, [dX, dY])

	def print_board(self, board = None, onlyId = False):
		if not board:
			board = self.board
		print("---------------")
		for i in board:
			rowInd = 0
			run = True
			if onlyId:
				outStr = ""
				for t in i:
					if t:
						outStr += t.tileID + "  "
					else:
						outStr += "XXXX  "
				print(outStr)

			else:
				while run:
					outStr = ""
					oFound = False
					for t in i:
						if t:
							if rowInd >= len(t.tileArray):
								break
							oFound = True
							outStr += t.get_row(rowInd) + "  "
						else:
							outStr += "            "
					rowInd += 1

					if not oFound:
						run = False
					print(outStr)


class Tile:
	def __init__(self, tileID, tileArray):
		self.tileID = tileID
		self.tileArray = tileArray

		self.isCorner = False
		self.flipH = 0
		self.flipV = 0

		lSide = ""
		rSide = ""
		for tileRow in tileArray:
			rSide += tileRow[len(tileRow) - 1]
			lSide += tileRow[0]

		self.edges = [[],[],[],[]]
		self.edges[0].append(tileArray[0])
		self.edges[0].append(tileArray[0][::-1])
		self.edges[1].append(rSide)
		self.edges[1].append(rSide[::-1])
		self.edges[2].append(tileArray[len(tileArray) - 1])
		self.edges[2].append(tileArray[len(tileArray) - 1][::-1])
		self.edges[3].append(lSide)
		self.edges[3].append(lSide[::-1])

		self.allEdges = []
		self.allEdges.append(tileArray[0])
		self.allEdges.append(tileArray[0][::-1])
		self.allEdges.append(rSide)
		self.allEdges.append(rSide[::-1])
		self.allEdges.append(tileArray[len(tileArray) - 1])
		self.allEdges.append(tileArray[len(tileArray) - 1][::-1])
		self.allEdges.append(lSide)
		self.allEdges.append(lSide[::-1])

		self.direction = 0

		self.possibleNeighbors = [[],[],[],[]]
		self.neighbors = [[],[],[],[]]

	def has_edge(self, edge):
		try:
			return self.edges.index(edge)
		except:
			return None

	def get_edge(self, dir):
		if dir in [0,2]:
			return self.edges[dir][self.flipH]
		if dir in [1,3]:
			return self.edges[dir][self.flipV]

	def get_rel_dir(self, dir):
		change = self.direction
		diff = dir - change

		if diff < 0:
			diff = 4 + diff

		return easyMod(diff)

	def rotate_tile(self, dir, deg = 1):
		if not dir in [1, -1]:
			raise "Argument 'dir' must be in [1, -1]"
		self.direction += dir * deg
		if self.direction < 0:
			self.direction = 4 + self.direction
		self.direction = easyMod(self.direction)

	def set_possible(self, tiles):
		for num, edge in enumerate(self.edges):
			for tile in tiles:
				if self.tileID == tile.tileID:
					continue
				if edge[0] in tile.allEdges or edge[1] in tile.allEdges:
					self.possibleNeighbors[num].append(tile.tileID)
			if len(self.possibleNeighbors[num]) == 0:
				self.neighbors[num] = None

		if self.neighbors.count(None) == 2:
			self.isCorner = True

	def find_edge(self, toFind):
		result = []
		for num, edges in enumerate(self.edges):
			if toFind == edges[0]:
				result.append([num, 0])
			elif toFind == edges[1]:
				result.append([num, 1])
		return result

	def get_row(self, rowInd):
		row = ""
		if self.direction == 0:
			row = self.tileArray[rowInd]
			if self.flipV:
				row = row[::-1]

		elif self.direction == 1:
			for i in self.tileArray:
				row += i[rowInd]
			if self.flipH:
				row = row[::-1]

		elif self.direction == 2:
			row = self.tileArray[len(self.tileArray) - (rowInd + 1)]
			if self.flipV:
				row = row[::-1]

		elif self.direction == 3:
			for i in self.tileArray:
				row += i[len(i) - (rowInd + 1)]
			if self.flipH:
				row = row[::-1]

		return row

	def orient_tile(self, dir, edge):
		foundEdge = self.find_edge(edge)[0]
		print(foundEdge)
		self.direction = easyMod(dir + 2) - foundEdge[0]
		if self.direction < 0:
			self.direction = 4 + self.direction

		print(self.direction)

		newEdge = self.get_edge(dir)
		if abs(self.direction - dir) >= 2:
			newEdge = newEdge[::-1]
		print(newEdge, edge)
		if newEdge[::-1] == edge:
			print("flipped")
			if dir in [0,2]:
				self.flipV = abs(self.flipV - 1)
			elif dir in [1,3]:
				self.flipH = abs(self.flipH - 1)

	def print_tile(self):
		pass


inFile = open("day20.in", "r").read().split("\n\n")

tiles = []

for tileData in inFile:
	split = tileData.split(":\n")
	r1 = re.match("Tile ([0-9]+)", split[0])
	tileID = r1.group(1)
	tileArray = split[1]

	tiles.append(Tile(tileID, tileArray.strip().split("\n")))

board = TileBoard(LENGTH, WIDTH, tiles)

board.print_board()

