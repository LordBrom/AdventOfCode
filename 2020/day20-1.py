import re
import math
import copy

ROTATE_RIGHT = -1
ROTATE_LEFT = 1

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

WIDTH = 3
LENGTH = 3
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

		count = 1

		for tile in self.tiles:
			self.tileIDs[tile.tileID] = tile
			tile.set_possible(self.tiles)
			#if tile.isCorner and tile.tileID == '1951':
			if tile.isCorner:
				count *= int(tile.tileID)
				#print(tile.tileID)
				startTile = tile
		print(count)
		return
		if startTile == None:
			raise "No corner tile found"

		if startTile.neighbors[0] == None and startTile.neighbors[1] == None:
			startTile.rotate_tile(ROTATE_LEFT)

		elif startTile.neighbors[1] == None and startTile.neighbors[2] == None:
			startTile.rotate_tile(ROTATE_RIGHT)
			startTile.rotate_tile(ROTATE_RIGHT)

		elif startTile.neighbors[2] == None and startTile.neighbors[3] == None:
			startTile.rotate_tile(ROTATE_RIGHT)

		self.board[0][0] = startTile

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

	def fill_board(self, tile, mockBoard, used = [], pos = [0, 0]):
		self.print_board(mockBoard)
		if tile.tileID in used:
			return False

		used.append(tile.tileID)
		#print(pos, tile)
		mockBoard[pos[0]][pos[1]] = tile
		#print(pos)
		#print(mockBoard)
		#self.print_board(mockBoard)
		if self.is_board_full(mockBoard):
			self.board = mockBoard

		for dir in [0,1,2,3]:
			relDir = tile.get_rel_dir(dir)

			#if tile.neighbors[dir] == None:
			#	continue
			dX = pos[0]
			dY = pos[1]
			if relDir == 0:
				dX -= 1
			elif relDir == 1:
				dY += 1
			elif relDir == 2:
				dX += 1
			elif relDir == 3:
				dY -= 1

			if dX < 0 or dY < 0:
				continue
			if dX >= self.length or dY >= self.width:
				continue

			#print(tile.tileID, dir, tile.direction, tile.possibleNeighbors)

			for n in tile.possibleNeighbors[relDir]:
				#print([dX, dY])
				nTiles = self.tileIDs[n].find_edge(tile.get_edge(relDir))
				for tiles in nTiles:
					#print(tiles)
					self.tileIDs[n].direction = tiles[0]
					if tile.isFlipped == 0:
						self.tileIDs[n].isFlipped = tiles[1]
					else:
						self.tileIDs[n].isFlipped = abs(tiles[1] - 1)
					self.fill_board(self.tileIDs[n], copy.deepcopy(mockBoard), copy.deepcopy(used), [dX, dY])

	def print_board(self, board):
		print("---------------")
		for i in board:
			outStr = ""
			for t in i:
				if t:
					outStr += t.tileID + " "
				else:
					outStr += "xxxx "
			print(outStr)


class Tile:
	def __init__(self, tileID, tileArray):
		self.tileID = tileID
		self.tileArray = tileArray

		self.isCorner = False
		self.isFlipped = 0

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
		#print("get_edge", self.tileID, self.direction, dir, self.isFlipped, self.edges[easyMod(dir + self.direction)][self.isFlipped])
		return self.edges[dir][self.isFlipped]

	def get_rel_dir(self, dir):
		if self.isFlipped == 0:
			change = self.direction
		else:
			change = self.direction

		diff = dir + change

		if diff < 0:
			print(diff, 4 + diff)
			diff = 4 + diff

		return easyMod(diff)


	# 1 = right
	# -1 = left
	def rotate_tile(self, dir, deg = 1):
		if not dir in [1, -1]:
			raise "Argument 'dir' must be in [1, -1]"
		self.direction += dir * deg
		if self.direction < 0:
			self.direction -= 4
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

print(board.board)
