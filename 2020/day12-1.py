DIRECTION = ['E', 'S', 'W', 'N']

def path_ship(path):
	east = 0
	north = 0
	shipFace = 0
	result = []

	for i in path:
		action = i[:1]
		value = int(i[1:])

		if action == 'F':
			action = DIRECTION[shipFace]

		if action == 'N':
			north += value
		elif action == 'S':
			north -= value
		elif action == 'E':
			east += value
		elif action == 'W':
			east -= value

		elif action == 'R':
			turn = value // 90
			shipFace = (shipFace + turn) % 4
		elif action == 'L':
			turn = value // 90
			shipFace = shipFace - turn % 4
			if shipFace < 0:
				shipFace = 4 + shipFace

		result.append([east, north])

	return abs(east) + abs(north)

inFile = open("day12.in", "r").read().split("\n")
inFile.pop()

print(path_ship(inFile))





