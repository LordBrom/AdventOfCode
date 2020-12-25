
inFile = open("day25.in", "r").read().split("\n")
inFile.pop()

cardKey = int(inFile[0])
doorKey = int(inFile[1])

cardSubject = 7
cardValue = 1
cardLoop = 0

while not cardValue == cardKey:
	cardLoop += 1
	cardValue *= cardSubject
	cardValue %= 20201227

doorSubject = 7
doorValue = 1
doorLoop = 0

while not doorValue == doorKey:
	doorLoop += 1
	doorValue *= doorSubject
	doorValue %= 20201227

lastLoop = cardLoop
lastSubject = doorKey
lastValue = 1

for i in range(lastLoop):
	lastValue *= lastSubject
	lastValue %= 20201227


print(lastValue)
