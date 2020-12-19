def path_wire(path):
	posx = 0
	posy = 0
	result = []
	for i in path:
		wireDir = i[:1]
		wireLen = i[1:]
		for i in range(int(wireLen)):
			if wireDir == 'R':
				posx += 1
			elif wireDir == 'L':
				posx -= 1
			elif wireDir == 'U':
				posy += 1
			elif wireDir == 'D':
				posy -= 1

			result.append([posx, posy])
	return result

def path_wires(wire1, wire2):
	wire1Path = []
	wire2Path = []
	posx = 0
	posy = 0
	for i in wire1:
		wireDir = i[:1]
		wireLen = i[1:]
		for i in range(int(wireLen)):
			if wireDir == 'R':
				posx += 1
			elif wireDir == 'L':
				posx -= 1
			elif wireDir == 'U':
				posy += 1
			elif wireDir == 'D':
				posy -= 1

			wire1Path.append([posx, posy])

	minDist = 0

	posx = 0
	posy = 0
	for i in wire2:
		wireDir = i[:1]
		wireLen = i[1:]
		for i in range(int(wireLen)):
			if wireDir == 'R':
				posx += 1
			elif wireDir == 'L':
				posx -= 1
			elif wireDir == 'U':
				posy += 1
			elif wireDir == 'D':
				posy -= 1

			wire2Path.append([posx, posy])
			if [posx, posy] in wire1Path:
				calcDist = (len(wire2Path)) + (wire1Path.index([posx, posy]))
				if minDist == 0:
					minDist = calcDist
				else:
					minDist = min(calcDist, minDist)
	return minDist + 1

inFile = open("day3.in", "r").read().split("\n")

wire1 = inFile[0].split(',')
wire2 = inFile[1].split(',')

print(path_wires(wire1, wire2))
