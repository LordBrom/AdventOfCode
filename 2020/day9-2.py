PREAMBLE = 25

def is_valid(num, validNums):
	for i in validNums:
		for j in validNums:
			if i == j:
				continue
			if int(i) + int(j) == int(num):
				return True
	return False

def check_sum(desire, nums):
	count = 0
	for num in nums:
		count += num
	return count == desire

inFile = open("day9.in", "r").read().split("\n")
inFile.pop()

for i in range(len(inFile)):
	inFile[i] = int(inFile[i])

numToFind = 0
maxNum = 0

for i in range(PREAMBLE, len(inFile)):
	nums = []
	for j in range(PREAMBLE):
		nums.append(inFile[(i - j) - 1])
	if not is_valid(inFile[i], nums):
		numToFind = inFile[i]
		maxNum = i


for i in range(len(inFile)):
	for j in range(i, maxNum):
		nums = inFile[i:j]

		if check_sum(numToFind, nums):
			nums.sort()
			print(nums[0] + nums[len(nums) - 1])

