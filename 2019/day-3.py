
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

wire1 = input("Enter wire 1:").split(',')
wire2 = input("Enter wire 2:").split(',')

wirePath1 = path_wire(wire1)
wirePath2 = path_wire(wire2)

crossPoints = [x for x in wirePath1 if x in wirePath2]
minDist = 0



#for i in wirePath1:
#	if i[0] == 0 and i[1] == 0:
#		continue
#	elif i in wirePath2:
#		crossPoints.append(i)
#		calcDist = abs(0 - i[0]) + abs(0 - i[1])
#		if minDist == 0:
#			minDist = calcDist
#		else:
#			minDist = min(calcDist, minDist)

print(crossPoints)


