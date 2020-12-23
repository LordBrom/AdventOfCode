


inFile = open("day23.in", "r").read().strip()

cups = [int(x) for x in inFile]

cups += [x for x in range(len(cups) + 1, 1000001)]

minVal = sorted(cups)[0]
maxVal = sorted(cups)[len(cups) - 1]

currentCup = 0
count = 0
for i in range(10000000):
	count += 1
	curLabel = cups[currentCup]

	if currentCup < len(cups) - 3:
		outCups = cups[currentCup + 1: currentCup + 4]
		cups = [x for n,x in enumerate(cups) if not (n > currentCup and n <= currentCup + 3)]
	else:
		outCups = cups[currentCup + 1:] + cups[:4 - (len(cups) - currentCup)]
		cups = [x for n,x in enumerate(cups) if not (n > currentCup or n <= 3 - (len(cups) - currentCup))]

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

cup1 = cups.index(1)

r1 = cup1 + 1
r2 = cup1 + 2

if r1 == len(cups):
	r1 = 0
	r2 = 1
elif r2 == len(cups):
	r2 = 0

print(cups[r1])
print(cups[r2])
print(cups[r1] * cups[r2])

