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

		result = 1
		for tile in self.tiles:
			tile.set_possible(self.tiles)
			if tile.isCorner:
				result *= int(tile.tileID)

		print(result)

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

inFile = open("day20.in", "r").read().split("\n\n")

tiles = []

for tileData in inFile:
	split = tileData.split(":\n")
	r1 = re.match("Tile ([0-9]+)", split[0])
	tileID = r1.group(1)
	tileArray = split[1]

	tiles.append(Tile(tileID, tileArray.strip().split("\n")))

board = TileBoard(LENGTH, WIDTH, tiles)

