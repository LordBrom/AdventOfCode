PREAMBLE = 25

def is_valid(num, validNums):
	for i in validNums:
		for j in validNums:
			if i == j:
				continue
			if int(i) + int(j) == int(num):
				return True
	return False

inFile = open("day9.in", "r").read().split("\n")
inFile.pop()

for i in range(PREAMBLE, len(inFile)):
	nums = []
	for j in range(PREAMBLE):
		nums.append(inFile[(i - j) - 1])
	if not is_valid(inFile[i], nums):
		print(inFile[i])
