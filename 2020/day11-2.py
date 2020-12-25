
class SeatingArea:
	def __init__(self, seatInput):
		self.seats = []
		self.create_chair_array(seatInput)

	def create_chair_array(self, seatInput):
		for row in seatInput:
			newRow = []
			for seat in row:
				if seat == "L":
					newRow.append(False)
				else:
					newRow.append("0")
			self.seats.append(newRow)

	def print_seats(self):
		for row in self.seats:
			rowPrint = ""
			for seat in row:
				if seat == "0":
					rowPrint += "."
				elif seat == True:
					rowPrint += "#"
				else:
					rowPrint += "L"
			print(rowPrint)

	def count_occupied(self):
		count = 0
		for row in self.seats:
			for seat in row:
				if seat == True:
					count += 1
		return count

	def pass_time(self):
		change = False
		newSeats = []
		for row in range(len(self.seats)):
			newRow = []
			for col in range(len(self.seats[row])):

				if self.seats[row][col] == "0":
					newRow.append("0")
				elif self.seats[row][col] == True:
					if self.check_adjacent(row, col) >= 5:
						newRow.append(False)
						change = True
					else:
						newRow.append(True)
				else:
					if self.check_adjacent(row, col) == 0:
						newRow.append(True)
						change = True
					else:
						newRow.append(False)
			newSeats.append(newRow)
		self.seats = newSeats
		return change

	def check_adjacent(self, row, col):
		count = 0

		found = [[False, False, False],[False, True, False],[False, False, False]]

		run = True

		n = 1
		while run:
			for i in [1, 0, -1]:
				for j in [1, 0, -1]:
					if i == 0 and j == 0:
						continue
					rowCheck = row + (i * n)
					colCheck = col + (j * n)

					if found[i+1][j+1]:
						continue

					if rowCheck < 0 or colCheck < 0:
						found[i+1][j+1] = True
						continue
					if rowCheck >= len(self.seats):
						found[i+1][j+1] = True
						continue
					if colCheck >= len(self.seats[rowCheck]):
						found[i+1][j+1] = True
						continue

					if self.seats[rowCheck][colCheck] == "0":
						pass
					elif self.seats[rowCheck][colCheck] == True:
						found[i+1][j+1] = True
						count += 1
					else:
						found[i+1][j+1] = True
			n += 1
			run = False
			for ifound in found:
				for jfound in ifound:
					if not jfound:
						run = True
		return count

inFile = open("day11.in", "r").read().split("\n")
inFile.pop()

area = SeatingArea(inFile)
iteration = 0
while area.pass_time():
	pass
print(area.count_occupied())

