DIRECTION = ['E', 'S', 'W', 'N']

def path_ship(path):
	east = 0
	north = 0

	waypointEast = 10
	waypointNorth = 1

	result = []

	for i in path:
		action = i[:1]
		value = int(i[1:])

		if action == 'F':
			east += waypointEast * value
			north += waypointNorth * value

		if action == 'N':
			waypointNorth += value
		elif action == 'S':
			waypointNorth -= value
		elif action == 'E':
			waypointEast += value
		elif action == 'W':
			waypointEast -= value

		elif action == 'R':
			turn = value // 90

			for i in range(turn):
				swapNorth = waypointNorth
				waypointNorth = waypointEast * -1
				waypointEast = swapNorth

		elif action == 'L':
			turn = value // 90

			for i in range(turn):
				swapEast = waypointEast
				waypointEast = waypointNorth * -1
				waypointNorth = swapEast

		result.append([east, north])

	return abs(east) + abs(north)

inFile = open("day12.in", "r").read().split("\n")
inFile.pop()

print(path_ship(inFile))





