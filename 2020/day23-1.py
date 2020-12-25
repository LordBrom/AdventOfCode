
inFile = open("day23.in", "r").read().strip()

cups = [int(x) for x in inFile]

minVal = sorted(cups)[0]
maxVal = sorted(cups)[-1]

currentCup = 0
count = 0
for i in range(100):
	count += 1
	curLabel = cups[currentCup]

	if currentCup < len(cups) - 4:
		outCups = cups[currentCup + 1: currentCup + 4]
		cups = cups[:currentCup + 1] + cups[4 - (len(cups) - currentCup):]
	else:
		outCups = cups[currentCup + 1:] + cups[:4 - (len(cups) - currentCup)]
		cups = cups[4 - (len(cups) - currentCup):currentCup + 1]

	destination = cups[min(currentCup, len(cups) - 1)] - 1

	while destination in outCups or destination < minVal:
		destination -= 1
		if destination < minVal:
			destination = maxVal

	destPos = cups.index(destination)

	cups = cups[:destPos + 1] + outCups + cups[destPos + 1:]

	currentCup = cups.index(curLabel)

	currentCup += 1
	currentCup = currentCup % len(cups)

while cups.index(1) != 0:
	cups.append(cups.pop(0))

cups.pop(0)

print(''.join(str(x) for x in cups))
