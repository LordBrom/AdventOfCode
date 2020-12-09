import itertools

def get_num(intcode, pos, mode = 0):
	if mode == 0:
		return int(intcode[int(intcode[pos])])
	elif mode == 1:
		return int(intcode[pos])

def set_num(intcode, pos, val, mode = 0):
	if mode == 0:
		intcode[int(intcode[pos])] = str(val)
	elif mode == 1:
		intcode[pos] = str(val)
	return intcode

def get_op_code(intcode, pos):
	opCode = intcode[pos][::-1]
	opCode += ('0' * (5 - len(opCode)))
	return opCode

def previous_amp(num, maxAmp):
	if num == 0:
		return maxAmp
	else:
		return num - 1

def intcode_computer(intcode, input1, input2):

	opCodePos = 0
	opCodeFull = get_op_code(intcode, opCodePos)
	opCode = opCodeFull[:2]

	outputVal = 0

	while opCode != '99':
		if opCode == '10':
			arg1 = get_num(intcode, opCodePos + 1, int(opCodeFull[2]) or 0)
			arg2 = get_num(intcode, opCodePos + 2, int(opCodeFull[3]) or 0)
			val = arg1 + arg2

			intcode = set_num(intcode, opCodePos + 3, val, int(opCodeFull[4]) or 0)
			opCodePos += 4

		elif opCode == '20':
			arg1 = get_num(intcode, opCodePos + 1, int(opCodeFull[2]) or 0)
			arg2 = get_num(intcode, opCodePos + 2, int(opCodeFull[3]) or 0)
			val = arg1 * arg2
			intcode = set_num(intcode, opCodePos + 3, val, int(opCodeFull[4]) or 0)
			opCodePos += 4

		elif opCode == '30':
			if opCodePos == 0:
				val = input1
			else:
				val = input2
			intcode = set_num(intcode, opCodePos + 1, val, int(opCodeFull[2]) or 0)
			opCodePos += 2

		elif opCode == '40':
			return get_num(intcode, opCodePos + 1, int(opCodeFull[2]) or 0)

		elif opCode == '50':
			arg1 = get_num(intcode, opCodePos + 1, int(opCodeFull[2]) or 0)
			if arg1 != 0:
				opCodePos = get_num(intcode, opCodePos + 2, int(opCodeFull[3]) or 0)
			else:
				opCodePos += 3

		elif opCode == '60':
			arg1 = get_num(intcode, opCodePos + 1, int(opCodeFull[2]) or 0)
			if arg1 == 0:
				opCodePos = get_num(intcode, opCodePos + 2, int(opCodeFull[3]) or 0)
			else:
				opCodePos += 3

		elif opCode == '70':
			arg1 = get_num(intcode, opCodePos + 1, int(opCodeFull[2]) or 0)
			arg2 = get_num(intcode, opCodePos + 2, int(opCodeFull[3]) or 0)
			if arg1 < arg2:
				intcode = set_num(intcode, opCodePos + 3, 1, int(opCodeFull[4]) or 0)
			else:
				intcode = set_num(intcode, opCodePos + 3, 0, int(opCodeFull[4]) or 0)
			opCodePos += 4

		elif opCode == '80':
			arg1 = get_num(intcode, opCodePos + 1, int(opCodeFull[2]) or 0)
			arg2 = get_num(intcode, opCodePos + 2, int(opCodeFull[3]) or 0)
			if arg1 == arg2:
				intcode = set_num(intcode, opCodePos + 3, 1, int(opCodeFull[4]) or 0)
			else:
				intcode = set_num(intcode, opCodePos + 3, 0, int(opCodeFull[4]) or 0)
			opCodePos += 4

		opCodeFull = get_op_code(intcode, opCodePos)
		opCode = opCodeFull[:2]
	return outputVal

inFile = open("day7.in", "r").read().split(",")

lastOutput = 0
maxOutput = 0
for pattern in itertools.permutations(range(5), 5):
	lastOutput = 0
	for i in pattern:
		lastOutput = intcode_computer(inFile, i, lastOutput)
	maxOutput = max(maxOutput, lastOutput)

print(maxOutput)
