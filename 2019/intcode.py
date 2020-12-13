
class IntcodeComputer:
	def __init__(self, intcode, debug = False):
		self.intcode = []
		for i in intcode:
			self.intcode.append(int(i))
		self.pointer = 0
		self.opCodeFull = ""
		self.opCode = ""
		self.relBase = 0

		self.debug = debug

	def debug_print(self, message):
		if self.debug:
			print(message)

	def get_intcode(self):
		return self.intcode

	def get_op_code(self):
		return self.opCode

	def get_mode(self, pos):
		return int(self.opCodeFull[pos]) or 0

	def get_pos(self, offset, mode):
		print(offset, mode, self.relBase)
		if mode == 0: # position mode
			return self.intcode[offset]
		elif mode == 1: # immediate mode
			return offset
		elif mode == 2: # relative mode
			return self.intcode[self.relBase + offset]

	def get_num(self, arg):
		mode = self.get_mode(arg + 1)
		pos = self.get_pos(self.pointer + arg, mode)
		return self.intcode[pos]

	def set_num(self, arg, val):
		mode = self.get_mode(arg + 1)
		pos = self.get_pos(self.pointer + arg, mode)
		self.intcode[pos] = val

	def parse_op_code(self):
		self.opCodeFull = str(self.intcode[self.pointer])[::-1]
		self.opCodeFull += ('0' * (5 - len(self.opCodeFull)))
		self.opCode = self.opCodeFull[:2]

	def run(self, inpVal = ""):

		self.parse_op_code()

		outputVal = 0
		inputUsed = False

		while self.opCode != '99':
			self.debug_print(["pointer", self.pointer, "opCodeFull", self.opCodeFull, "opcode", self.opCode])
			if self.opCode == '10':
				arg1 = self.get_num(1)
				arg2 = self.get_num(2)
				val = arg1 + arg2
				self.debug_print([arg1, "+", arg2, "=", val])

				self.set_num(3, val)
				self.pointer += 4

			elif self.opCode == '20':
				arg1 = self.get_num(1)
				arg2 = self.get_num(2)
				val = arg1 * arg2
				self.debug_print([arg1, "*", arg2, "=", val])

				self.set_num(3, val)
				self.pointer += 4

			elif self.opCode == '30':
				if inputUsed:
					return outputVal
				if inpVal == "":
					inpVal = input("Needs input: ")
				val = inpVal
				inputUsed = True
				self.debug_print(["setting", val])
				self.set_num(1, val)
				self.pointer += 2

			elif self.opCode == '40':
				self.debug_print(["output", self.get_num(1)])
				outputVal = self.get_num(1)
				self.pointer += 2

			elif self.opCode == '50':
				arg1 = self.get_num(1)
				if arg1 != 0:
					self.pointer = self.get_num(2)
				else:
					self.pointer += 3

			elif self.opCode == '60':
				arg1 = self.get_num(1)
				if arg1 == 0:
					self.pointer = self.get_num(2)
				else:
					self.pointer += 3

			elif self.opCode == '70':
				arg1 = self.get_num(1)
				arg2 = self.get_num(2)
				if arg1 < arg2:
					self.set_num(3, 1)
				else:
					self.set_num(3, 0)
				self.pointer += 4

			elif self.opCode == '80':
				arg1 = self.get_num(1)
				arg2 = self.get_num(2)
				if arg1 == arg2:
					self.set_num(3, 1)
				else:
					self.set_num(3, 0)
				self.pointer += 4

			elif self.opCode == '90':
				arg1 = self.get_num(1)
				print(["relBase from", self.relBase, "to", arg1])
				self.relBase += arg1
				self.pointer += 2

			else:
				print("bad op code:", self.opCode, self.opCodeFull, self.pointer)
				return

			self.parse_op_code()

		return outputVal
