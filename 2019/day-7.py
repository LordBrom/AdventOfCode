import itertools

OPCODE_POS = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
OPCODE_MEMORY = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

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

def intcode_computer(intcode, inputPattern):

	#opCodePos = 0
	currentAmp = 0
	maxAmp = 5
	opCodePos = [0, 0, 0, 0, 0]
	opCodeInput = [0, "", "", "", ""]
	opCodeFull = get_op_code(intcode, opCodePos[currentAmp])
	opCode = opCodeFull[:2]
	intcodeList = [intcode,intcode,intcode,intcode,intcode]

	outputVal = 0

	while opCode != '99':
		if opCode == '10':
			arg1 = get_num(intcodeList[currentAmp], opCodePos[currentAmp] + 1, int(opCodeFull[2]) or 0)
			arg2 = get_num(intcodeList[currentAmp], opCodePos[currentAmp] + 2, int(opCodeFull[3]) or 0)
			val = arg1 + arg2

			intcodeList[currentAmp] = set_num(intcodeList[currentAmp], opCodePos[currentAmp] + 3, val, int(opCodeFull[4]) or 0)
			opCodePos[currentAmp] += 4

		elif opCode == '20':
			arg1 = get_num(intcodeList[currentAmp], opCodePos[currentAmp] + 1, int(opCodeFull[2]) or 0)
			arg2 = get_num(intcodeList[currentAmp], opCodePos[currentAmp] + 2, int(opCodeFull[3]) or 0)
			val = arg1 * arg2
			intcodeList[currentAmp] = set_num(intcodeList[currentAmp], opCodePos[currentAmp] + 3, val, int(opCodeFull[4]) or 0)
			opCodePos[currentAmp] += 4

		elif opCode == '30':
			if opCodePos[currentAmp] == 0:
				intcodeList[currentAmp] = set_num(intcodeList[currentAmp], opCodePos[currentAmp] + 1, currentAmp + 5, int(opCodeFull[2]) or 0)
				opCodePos[currentAmp] += 2
			else:
				if opCodeInput[currentAmp] == "":
					currentAmp += 1
					currentAmp = currentAmp % maxAmp
				else:
					val = opCodeInput[currentAmp]
					print(intcodeList[currentAmp])
					intcodeList[currentAmp] = set_num(intcodeList[currentAmp], opCodePos[currentAmp] + 1, val, int(opCodeFull[2]) or 0)
					print(intcodeList[currentAmp])
					opCodePos[currentAmp] += 2
					opCodeInput[currentAmp] = ""

		elif opCode == '40':
			nextAmp = currentAmp + 1
			nextAmp = nextAmp % maxAmp
			opCodeInput[nextAmp] = get_num(intcodeList[currentAmp], opCodePos[currentAmp] + 1, int(opCodeFull[2]) or 0)
			opCodePos[currentAmp] += 2

		elif opCode == '50':
			arg1 = get_num(intcodeList[currentAmp], opCodePos[currentAmp] + 1, int(opCodeFull[2]) or 0)
			if arg1 != 0:
				opCodePos[currentAmp] = get_num(intcodeList[currentAmp], opCodePos[currentAmp] + 2, int(opCodeFull[3]) or 0)
			else:
				opCodePos[currentAmp] += 3

		elif opCode == '60':
			arg1 = get_num(intcodeList[currentAmp], opCodePos[currentAmp] + 1, int(opCodeFull[2]) or 0)
			if arg1 == 0:
				opCodePos[currentAmp] = get_num(intcodeList[currentAmp], opCodePos[currentAmp] + 2, int(opCodeFull[3]) or 0)
			else:
				opCodePos[currentAmp] += 3

		elif opCode == '70':
			arg1 = get_num(intcodeList[currentAmp], opCodePos[currentAmp] + 1, int(opCodeFull[2]) or 0)
			arg2 = get_num(intcodeList[currentAmp], opCodePos[currentAmp] + 2, int(opCodeFull[3]) or 0)
			if arg1 < arg2:
				intcodeList[currentAmp] = set_num(intcodeList[currentAmp], opCodePos[currentAmp] + 3, 1, int(opCodeFull[4]) or 0)
			else:
				intcodeList[currentAmp] = set_num(intcodeList[currentAmp], opCodePos[currentAmp] + 3, 0, int(opCodeFull[4]) or 0)
			opCodePos[currentAmp] += 4

		elif opCode == '80':
			arg1 = get_num(intcodeList[currentAmp], opCodePos[currentAmp] + 1, int(opCodeFull[2]) or 0)
			arg2 = get_num(intcodeList[currentAmp], opCodePos[currentAmp] + 2, int(opCodeFull[3]) or 0)
			if arg1 == arg2:
				intcodeList[currentAmp] = set_num(intcodeList[currentAmp], opCodePos[currentAmp] + 3, 1, int(opCodeFull[4]) or 0)
			else:
				intcodeList[currentAmp] = set_num(intcodeList[currentAmp], opCodePos[currentAmp] + 3, 0, int(opCodeFull[4]) or 0)
			opCodePos[currentAmp] += 4

		opCodeFull = get_op_code(intcodeList[currentAmp], opCodePos[currentAmp])
		opCode = opCodeFull[:2]
	return outputVal

inFile = open("day-7.in", "r").read().split("\n")
inFile.pop()
code = inFile[0].split(",")

maxOutput = 0
for pattern in itertools.permutations(range(5), 5):
	lastOutput = intcode_computer(code, pattern)
	maxOutput = max(maxOutput, int(lastOutput))


#intcode_computer(inFile[0].split(","))
