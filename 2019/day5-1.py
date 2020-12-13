debug = False

from intcode import IntcodeComputer

#def get_num(intcode, pos, mode = 0):
#	if mode == 0:
#		return int(intcode[int(intcode[pos])])
#	elif mode == 1:
#		return int(intcode[pos])

#def set_num(intcode, pos, val, mode = 0):
#	if mode == 0:
#		intcode[int(intcode[pos])] = str(val)
#	elif mode == 1:
#		intcode[pos] = str(val)
#	return intcode

#def get_op_code(intcode, pos):
#	opCode = intcode[pos][::-1]
#	opCode += ('0' * (5 - len(opCode)))
#	return opCode

#def intcode_computer(intcode):
#	count = 0
#	opCodePos = 0
#	opCodeFull = get_op_code(intcode, opCodePos)
#	opCode = opCodeFull[:2]
#	print("")
#	while opCode != '99':
#		count += 1
#		if opCode == '10':
#			arg1 = get_num(intcode, opCodePos + 1, int(opCodeFull[2]) or 0)
#			arg2 = get_num(intcode, opCodePos + 2, int(opCodeFull[3]) or 0)
#			val = arg1 + arg2

#			intcode = set_num(intcode, opCodePos + 3, val, int(opCodeFull[4]) or 0)
#			opCodePos += 4

#		elif opCode == '20':
#			arg1 = get_num(intcode, opCodePos + 1, int(opCodeFull[2]) or 0)
#			arg2 = get_num(intcode, opCodePos + 2, int(opCodeFull[3]) or 0)
#			val = arg1 * arg2
#			intcode = set_num(intcode, opCodePos + 3, val, int(opCodeFull[4]) or 0)
#			opCodePos += 4

#		elif opCode == '30':
#			val = input("Enter Code: ")
#			set_num(intcode, opCodePos + 1, val, int(opCodeFull[2]) or 0)
#			opCodePos += 2

#		elif opCode == '40':
#			print("Output: " + str(get_num(intcode, opCodePos + 1, int(opCodeFull[2]) or 0)))
#			opCodePos += 2

#		else:
#			raise Exception("Invalid op code: " + str(opCode))

#		opCodeFull = get_op_code(intcode, opCodePos)
#		opCode = opCodeFull[:2]

#	return intcode

inFile = open("day5.in", "r").read().split(",")
comp = IntcodeComputer(inFile)
print(comp.run(1))

#intcode_computer(inFile[0].split(","))
