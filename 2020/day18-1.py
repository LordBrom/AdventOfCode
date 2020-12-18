import copy

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

def evaluateExp(exp):
	result = None
	# 0 = +
	# 1 = *
	op = 0
	i = 0
	while i < len(exp):
		n = exp[i]
		if n == " ":
			pass
		elif n == "+":
			op = 0
		elif n == "*":
			op = 1
		elif n == "(":
			endPos = getEndPar(exp[i + 1:])
			ls = copy.deepcopy(exp[:i])
			rs = copy.deepcopy(exp[i + endPos + 2:])

			num = evaluateExp(copy.deepcopy(exp[i + 1:i + endPos + 1]))
			exp = ls + str(num) + rs

			i -= 1
		elif n == ")":
			pass
		else:
			nSpace = exp.find(" ", i)
			if nSpace == -1:
				nSpace = exp.find(")", i)
			if nSpace == -1:
				nSpace = len(exp)
			num = exp[i:nSpace]

			if not result:
				result = int(num)
			elif op == 0:
				result += int(num)
			else:
				result *= int(num)
			i += len(num)
		i += 1

	return result

inFile = open("day18.in", "r").read().split("\n")
inFile.pop()

result = 0

for e in inFile:
	nR = evaluateExp(e)
	result += nR

print(result)
