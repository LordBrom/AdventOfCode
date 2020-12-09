import itertools
import copy

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

def next_amp(num, maxAmp):
	if num == maxAmp - 1:
		return 0
	else:
		return num + 1

def intcode_computer(intcode, pattern):

	curAmp = 0
	lastOutput = 0
	aryIntcode = []
	aryPointer = []

	for i in range(len(pattern)):
		aryIntcode.append(copy.deepcopy(intcode))
		aryPointer.append(0)

	opCodeFull = get_op_code(aryIntcode[curAmp], aryPointer[curAmp])
	opCode = opCodeFull[:2]

	while opCode != '99' or curAmp != 4:
		#print(str(curAmp) + " : " + str(opCode))
		if opCode == '99':
			curAmp = next_amp(curAmp, 5)
		elif opCode == '10':
			arg1 = get_num(aryIntcode[curAmp], aryPointer[curAmp] + 1, int(opCodeFull[2]) or 0)
			arg2 = get_num(aryIntcode[curAmp], aryPointer[curAmp] + 2, int(opCodeFull[3]) or 0)
			val = arg1 + arg2

			aryIntcode[curAmp] = set_num(aryIntcode[curAmp], aryPointer[curAmp] + 3, val, int(opCodeFull[4]) or 0)
			aryPointer[curAmp] += 4

		elif opCode == '20':
			arg1 = get_num(aryIntcode[curAmp], aryPointer[curAmp] + 1, int(opCodeFull[2]) or 0)
			arg2 = get_num(aryIntcode[curAmp], aryPointer[curAmp] + 2, int(opCodeFull[3]) or 0)
			val = arg1 * arg2
			aryIntcode[curAmp] = set_num(aryIntcode[curAmp], aryPointer[curAmp] + 3, val, int(opCodeFull[4]) or 0)
			aryPointer[curAmp] += 4

		elif opCode == '30':
			if aryPointer[curAmp] == 0:
				val = pattern[curAmp] + 5
			else:
				val = lastOutput
			aryIntcode[curAmp] = set_num(aryIntcode[curAmp], aryPointer[curAmp] + 1, val, int(opCodeFull[2]) or 0)
			aryPointer[curAmp] += 2

		elif opCode == '40':
			lastOutput = get_num(aryIntcode[curAmp], aryPointer[curAmp] + 1, int(opCodeFull[2]) or 0)
			aryPointer[curAmp] += 2
			curAmp = next_amp(curAmp, 5)

		elif opCode == '50':
			arg1 = get_num(aryIntcode[curAmp], aryPointer[curAmp] + 1, int(opCodeFull[2]) or 0)
			if arg1 != 0:
				aryPointer[curAmp] = get_num(aryIntcode[curAmp], aryPointer[curAmp] + 2, int(opCodeFull[3]) or 0)
			else:
				aryPointer[curAmp] += 3

		elif opCode == '60':
			arg1 = get_num(aryIntcode[curAmp], aryPointer[curAmp] + 1, int(opCodeFull[2]) or 0)
			if arg1 == 0:
				aryPointer[curAmp] = get_num(aryIntcode[curAmp], aryPointer[curAmp] + 2, int(opCodeFull[3]) or 0)
			else:
				aryPointer[curAmp] += 3

		elif opCode == '70':
			arg1 = get_num(aryIntcode[curAmp], aryPointer[curAmp] + 1, int(opCodeFull[2]) or 0)
			arg2 = get_num(aryIntcode[curAmp], aryPointer[curAmp] + 2, int(opCodeFull[3]) or 0)
			if arg1 < arg2:
				aryIntcode[curAmp] = set_num(aryIntcode[curAmp], aryPointer[curAmp] + 3, 1, int(opCodeFull[4]) or 0)
			else:
				aryIntcode[curAmp] = set_num(aryIntcode[curAmp], aryPointer[curAmp] + 3, 0, int(opCodeFull[4]) or 0)
			aryPointer[curAmp] += 4

		elif opCode == '80':
			arg1 = get_num(aryIntcode[curAmp], aryPointer[curAmp] + 1, int(opCodeFull[2]) or 0)
			arg2 = get_num(aryIntcode[curAmp], aryPointer[curAmp] + 2, int(opCodeFull[3]) or 0)
			if arg1 == arg2:
				aryIntcode[curAmp] = set_num(aryIntcode[curAmp], aryPointer[curAmp] + 3, 1, int(opCodeFull[4]) or 0)
			else:
				aryIntcode[curAmp] = set_num(aryIntcode[curAmp], aryPointer[curAmp] + 3, 0, int(opCodeFull[4]) or 0)
			aryPointer[curAmp] += 4
		else:
			return lastOutput

		opCodeFull = get_op_code(aryIntcode[curAmp], aryPointer[curAmp])
		opCode = opCodeFull[:2]
	return lastOutput

inFile = open("day7.in", "r").read().split(",")


lastOutput = 0
maxOutput = 0
for pattern in itertools.permutations(range(5), 5):
	lastOutput = intcode_computer(inFile, pattern)
	maxOutput = max(maxOutput, lastOutput)

print(maxOutput)
