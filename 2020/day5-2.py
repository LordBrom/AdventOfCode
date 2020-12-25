import math

def find_seat(seatCode):
	frontBack = seatCode[:7]
	leftRight = seatCode[7:]

	lowerBound = 0
	upperBound = 127

	for i in frontBack:
		if i == 'F':
			upperBound -= math.ceil((upperBound - lowerBound) / 2)
		elif i == 'B':
			lowerBound += math.ceil((upperBound - lowerBound) / 2)

	row = upperBound

	lowerBound = 0
	upperBound = 7

	for i in leftRight:
		if i == 'L':
			upperBound -= math.ceil((upperBound - lowerBound) / 2)
		elif i == 'R':
			lowerBound += math.ceil((upperBound - lowerBound) / 2)

	col = upperBound

	return (row * 8) + col

inFile = open("day5.in", "r").read().split("\n")
inFile.pop()

maxSeat = 0
minSeat = 9999
seats = []
for seat in inFile:
	maxSeat = max(maxSeat, find_seat(seat))
	minSeat = min(minSeat, find_seat(seat))
	seats.append(find_seat(seat))

seats.sort()

mySeat = [x for x in range(minSeat, maxSeat) if x not in seats][0]

print(mySeat)
