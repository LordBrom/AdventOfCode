import copy

def intcode_computer(intcode):
	opCodePos = 0
	opCode = int(intcode[opCodePos])
	step = 0
	while opCode != 99:
		step += 1

		num1Pos = int(intcode[opCodePos + 1])
		num2Pos = int(intcode[opCodePos + 2])
		resPos = int(intcode[opCodePos + 3])

		num1 = int(intcode[num1Pos])
		num2 = int(intcode[num2Pos])

		result = 0
		if opCode == 1:
			result = num1 + num2
		elif opCode == 2:
			result = num1 * num2

		intcode[resPos] = result

		opCodePos += 4
		opCode = int(intcode[opCodePos])

	return intcode[0]

inFile = open("day2.in", "r").read().split(",")

inFile[1] = 12
inFile[2] = 2

print(intcode_computer(inFile))

