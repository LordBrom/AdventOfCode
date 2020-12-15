inFile = open("day14.in", "r").read().split("\n")
inFile.pop()

def set_value(value, inp, mask):
	value = value[::-1]
	mask = mask[::-1]
	result = ''
	inpBin = bin(inp)[2:][::-1]
	inpBin += '0' * (len(value) - len(inpBin))

	for i, num in enumerate(value):
		if mask[i] == 'X':
			if len(inpBin) > i:
				result += inpBin[i]
			else:
				result += num
		else:
			result += mask[i]
	return result[::-1]

mask = ""
value = '0' * 36

memory = {}

for i in inFile:
	iSplit = i.split(" = ")
	if iSplit[0] == "mask":
		mask = iSplit[1]
	else:
		memorySpace = iSplit[0][4:-1]
		if not memorySpace in memory:
			memory[memorySpace] = value
		memory[memorySpace] = set_value(memory[memorySpace], int(iSplit[1]), mask)

count = 0
for mem in memory:
	count += int(memory[mem], 2)

print(count)
