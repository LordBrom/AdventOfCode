from intcode import IntcodeComputer

BLACK = "0"
WHITE = "1"

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

class PaintJob:
	def __init__(self, width = 125):
		self.botPosX = width // 2
		self.botPosY = width // 2
		self.botFace = 0
		self.paint = []
		self.painted = []

		for row in range(width):
			newRow = []
			for col in range(width):
				newRow.append(BLACK)
			self.paint.append(newRow)

	def print_job(self):
		for row in self.paint:
			print("".join(row))

	def turn_bot(self, dir):
		if dir == 0:
			self.botFace -= 1
			if self.botFace < 0:
				self.botFace = 3
		else:
			self.botFace += 1
			if self.botFace > 3:
				self.botFace = 0


	def start_job(self, intCode):
		comp = IntcodeComputer(intCode)
		while True:
			if not [self.botPosX, self.botPosY] in self.painted:
				self.painted.append([self.botPosX, self.botPosY])

			currColor = self.paint[self.botPosX][self.botPosY]
			res = comp.run(currColor, False)
			if len(res) == 0:
				return
			color = res[0]
			turn = res[1]
			self.paint[self.botPosX][self.botPosY] = str(color)

			self.turn_bot(turn)

			if self.botFace == 0:
				self.botPosX += 1
			elif self.botFace == 1:
				self.botPosY += 1
			elif self.botFace == 2:
				self.botPosX -= 1
			else:
				self.botPosY -= 1


inFile = open("day11.in", "r").read().split(",")

paintJob = PaintJob()
paintJob.start_job(inFile)

paintJob.print_job()

print(len(paintJob.painted))

