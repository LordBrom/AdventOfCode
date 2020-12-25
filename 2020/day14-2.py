inFile = open("day14.in", "r").read().split("\n")
inFile.pop()

def fix_floating(value):
	result = []

	xFind = value.find('X')
	if xFind == -1:
		result.append(value)
	else:
		value1 = value[:xFind] + '1' + value[xFind + 1:]
		value0 = value[:xFind] + '0' + value[xFind + 1:]

		result += fix_floating(value1)
		result += fix_floating(value0)

	return result


def get_address(value, inp, mask):
	value = value[::-1]
	mask = mask[::-1]
	result = ''
	inpBin = bin(inp)[2:][::-1]
	inpBin += '0' * (len(value) - len(inpBin))

	for i, num in enumerate(inpBin):
		if mask[i] == '0':
			result += num
		else:
			result += mask[i]

	addresses = fix_floating(result[::-1])
	return addresses

mask = ""
value = '0' * 36

memory = {}

for i in inFile:
	iSplit = i.split(" = ")
	if iSplit[0] == "mask":
		mask = iSplit[1]
	else:
		memorySpace = iSplit[0][4:-1]
		addresses = get_address(value, int(memorySpace), mask)
		for address in addresses:
			mem = int(address, 2)
			if not mem in memory:
				memory[mem] = value
			memory[mem] = int(iSplit[1])

count = 0
for mem in memory:
	count += memory[mem]

print(count)
