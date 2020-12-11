
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
					if self.check_adjacent(row, col) >= 4:
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
		for i in [1, 0, -1]:
			for j in [1, 0, -1]:
				if i == 0 and j == 0:
					continue
				rowCheck = row + i
				colCheck = col + j

				if rowCheck < 0 or colCheck < 0:
					continue
				if rowCheck >= len(self.seats):
					continue
				if colCheck >= len(self.seats[rowCheck]):
					continue

				if self.seats[rowCheck][colCheck] == True:
					count += 1
		return count

inFile = open("day11.in", "r").read().split("\n")
inFile.pop()

area = SeatingArea(inFile)
while area.pass_time():
	pass
print(area.count_occupied())

