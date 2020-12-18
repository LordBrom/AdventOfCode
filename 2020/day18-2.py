import copy

class expression:
	def __init__(self, num1, num2, op):
		self.num1 = num1
		self.num2 = num2
		self.op = op

def getEndPar(exp):
	pCount = 0
	for i, n in enumerate(exp):
		if pCount == 0 and n == ")":
			return i
		elif n == ")":
			pCount -= 1
		elif n == "(":
			pCount += 1
	return ""

def getNum(exp):
	nSpace = exp.find(" ")
	if nSpace == -1:
		nSpace = exp.find(")")
	if nSpace == -1:
		nSpace = len(exp)
	num = exp[:nSpace]
	return int(num)

def evaluateExp(exp):
	result = None
	exp = exp.split(" ")

	try:
		aPos = exp.index("+")
		while aPos != -1:
			exp = exp[:aPos - 1] + [int(exp[aPos - 1]) + int(exp[aPos + 1])] + exp[aPos + 2:]
			aPos = exp.index("+")
	except:
		pass

	try:
		tPos = exp.index("*")
		while tPos != -1:
			exp = exp[:tPos - 1] + [int(exp[tPos - 1]) * int(exp[tPos + 1])] + exp[tPos + 2:]
			tPos = exp.index("*")
	except:
		pass

	return str(exp[0])

def simplifyExp(exp):
	start = exp.find("(")
	while start != -1:
		end = getEndPar(exp[start + 1:])
		ls = exp[:start]
		rs = exp[start + end + 2:]
		newExp = ls + simplifyExp(exp[start + 1:start + end + 1]) + rs
		exp = newExp
		start = exp.find("(")
	return evaluateExp(exp)



inFile = open("day18.in", "r").read().split("\n")
inFile.pop()

result = 0

for e in inFile:
	#print(simplifyExp(e))
	nR = simplifyExp(e)
	result += int(nR)

print(result)
