inFile = open("day13.in", "r").read().split("\n")
inFile.pop()

depart = inFile[0]
busesRaw = inFile[1].split(",")
buses = []

for i in range(len(busesRaw)):
	if busesRaw[i] == 'x':
		continue
	buses.append([i, int(busesRaw[i])])

tVal = 0
busSync = buses[0][1]
busSyncList = [buses[0][1]]
while True:
	tVal += busSync
	found = True

	for offset, bus in buses:
		if bus == 0:
			continue

		if (tVal +  offset) % bus != 0:
			found = False
			break
		elif not bus in busSyncList:
			busSyncList.append(bus)
			busSync *= bus
	if found:
		break
print(tVal)
