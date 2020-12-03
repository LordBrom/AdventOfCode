debug = False

def debug_log(msg):
	if debug:
		print(msg)

def get_num(intcode, pos, mode = 0):
	if mode == 0:
		debug_log("Pulling " + intcode[int(intcode[pos])] + " from " + intcode[pos] + " via " + str(pos))
		return int(intcode[int(intcode[pos])])
	elif mode == 1:
		debug_log("Pulling " + intcode[pos] + " from " + str(pos))
		return int(intcode[pos])

def set_num(intcode, pos, val, mode = 0):
	if mode == 0:
		debug_log("Setting " + str(val) + " to " + intcode[pos] + " via " + str(pos))
		intcode[int(intcode[pos])] = str(val)
	elif mode == 1:
		debug_log("Setting " + str(val) + " to " + str(pos))
		intcode[pos] = str(val)
	return intcode

def get_op_code(intcode, pos):
	opCode = intcode[pos][::-1]
	opCode += ('0' * (5 - len(opCode)))
	return opCode


def intcode_computer(intcode):

	count = 0
	opCodePos = 0
	opCodeFull = get_op_code(intcode, opCodePos)
	opCode = opCodeFull[:2]
	print("")
	while opCode != '99':
		count += 1
		debug_log("step " + str(count) + ", running op code: " + opCode)
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
			val = input("Enter Code: ")
			set_num(intcode, opCodePos + 1, val, int(opCodeFull[2]) or 0)
			opCodePos += 2

		elif opCode == '40':
			print("Output: " + str(get_num(intcode, opCodePos + 1, int(opCodeFull[2]) or 0)))
			opCodePos += 2

		elif opCode == '50':
			arg1 = get_num(intcode, opCodePos + 1, int(opCodeFull[2]) or 0)
			debug_log("opCodePos " + str(opCodePos))
			if arg1 != 0:
				opCodePos = get_num(intcode, opCodePos + 2, int(opCodeFull[3]) or 0)
				debug_log("opCodePos " + str(opCodePos))
			else:
				opCodePos += 3

		elif opCode == '60':
			arg1 = get_num(intcode, opCodePos + 1, int(opCodeFull[2]) or 0)
			debug_log("opCodePos " + str(opCodePos))
			if arg1 == 0:
				opCodePos = get_num(intcode, opCodePos + 2, int(opCodeFull[3]) or 0)
				debug_log("opCodePos " + str(opCodePos))
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

		else:
			print("code pos: " + str(opCodePos))
			print("op code: " + str(opCodeFull))
			print(intcode)
			print("bad code: " + opCode)
			return

		debug_log(intcode)
		opCodeFull = get_op_code(intcode, opCodePos)
		opCode = opCodeFull[:2]
		debug_log("")

	return intcode

inFile = open("day-5.in", "r").read().split("\n")
inFile.pop()
intcode_computer(inFile[0].split(","))
