
import copy

class CubeSpace:
	def __init__(self, z, x, y, w):
		self.z = z
		self.x = x
		self.y = y
		self.w = w
		self.isActive = False

		self.nextState = False

		self.neighborPos = []
		self.neighbors = []

		for dz in [-1, 0, 1]:
			for dx in [-1, 0, 1]:
				for dy in [-1, 0, 1]:
					for dw in [-1, 0, 1]:
						if dx == 0 and dy == 0 and dz == 0 and dw == 0:
							continue
						self.neighborPos.append([z + dz, x + dx, y + dy, w + dw])

	def set_status(self, status):
		self.isActive = status
		self.nextState = status

	def set_next_status(self, status):
		self.nextState = status

	def use_next_status(self):
		self.isActive = copy.deepcopy(self.nextState)

	def set_neighbors(self, dimension):
		for dz, dx, dy, dw in self.neighborPos:
			if dx < 0 or dy < 0 or dz < 0 or dw < 0:
				continue
			elif dx >= len(dimension) or dy >= len(dimension) or dz >= len(dimension) or dw >= len(dimension):
				continue
			else:
				self.neighbors.append(dimension[dz][dx][dy][dw])

	def count_active_neignbors(self):
		count = 0
		for neighbor in self.neighbors:
			if neighbor.isActive:
				count += 1
		return count

	def pos(self, activeOnly = False):
		return [self.z, self.x, self.y, self.w]

class PocketDimension:
	def __init__(self, initialState):
		self.cubes = []

		width = 25

		for z in range(width):
			newPlain = []
			for x in range(width):
				newRow = []
				for y in range(width):
					newWrow = []
					for w in range(width):
						newWrow.append(CubeSpace(z, x, y, w))
					newRow.append(newWrow)
				newPlain.append(newRow)
			self.cubes.append(newPlain)

		for row, cubes in enumerate(initialState):
			for col, cube in enumerate(cubes):
				if cube == '#':
					self.cubes[len(self.cubes) // 2][len(self.cubes) // 2][(len(self.cubes) // 2) + row][(len(self.cubes) // 2) + col].set_status(True)

		for plain in self.cubes:
			for row in plain:
				for col in row:
					for wRow in col:
						wRow.set_neighbors(self.cubes)

	def print_plain(self, z):
		plain = self.cubes[z]
		for row in plain:
			outStr = ""
			for col in row:
				if col.isActive:
					outStr += "#"
				else:
					outStr += "."
			print(outStr)

	def print_all(self):
		for num, plain in enumerate(self.cubes):
			print("z=", len(self.cubes) // 2 - num)
			self.print_plain(num)

	def count_active(self):
		count = 0
		for plain in self.cubes:
			for row in plain:
				for col in row:
					for wRow in col:
						if wRow.isActive:
							count += 1
		return count

	def cycle(self):
		count = 0
		for plain in self.cubes:
			for row in plain:
				for col in row:
					for wRow in col:
						nCount = wRow.count_active_neignbors()
						if wRow.isActive:
							if nCount != 2 and nCount != 3:
								wRow.set_next_status(False)
								count += 1
						else:
							if nCount == 3:
								wRow.set_next_status(True)
								count += 1

		for plain in self.cubes:
			for row in plain:
				for col in row:
					for wRow in col:
						wRow.use_next_status()
		return count

inFile = open("day17.in", "r").read().split("\n")
inFile.pop()
dimension = PocketDimension(inFile)

dimension.cycle()
dimension.cycle()
dimension.cycle()
dimension.cycle()
dimension.cycle()
dimension.cycle()

print(dimension.count_active())
