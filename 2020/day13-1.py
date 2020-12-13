
inFile = open("day13.in", "r").read().split("\n")
inFile.pop()

depart = inFile[0]
buses = inFile[1].split(",")

run = True

count = 0

result = 0

while run:
	for bus in buses:
		if bus == 'x':
			continue
		if ((int(depart) + count) % int(bus)) == 0:
			result = (count * int(bus))
			run = False
	count += 1
print(result)
