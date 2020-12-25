blackTiles = []

inFile = open("day24.in", "r").read().split("\n")
inFile.pop()

for order in inFile:
	pos = [0, 0, 0]

	i = 0
	while i < len(order):
		direction = order[i]
		if not direction in ['e','w']:
			direction += order[i + 1]
			i += 1

		if direction == 'ne':
			pos[0] += 1
			pos[2] -= 1
		elif direction == 'sw':
			pos[0] -= 1
			pos[2] += 1
		elif direction == 'e':
			pos[0] += 1
			pos[1] -= 1
		elif direction == 'w':
			pos[0] -= 1
			pos[1] += 1
		elif direction == 'se':
			pos[1] -= 1
			pos[2] += 1
		elif direction == 'nw':
			pos[1] += 1
			pos[2] -= 1
		i += 1

	if pos in blackTiles:
		blackTiles.remove(pos)
	else:
		blackTiles.append(pos)

print(len(blackTiles))
