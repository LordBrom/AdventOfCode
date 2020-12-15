inFile = open("day15.in", "r").read().split("\n")
inFile.pop()

nums = inFile[0].split(",")
for i, val in enumerate(nums):
	nums[i] = int(val)

def list_rindex(li, x, b = None):
	if b:
		li = li[:b]
	for i in reversed(range(len(li))):
		if li[i] == x:
			return i
	return -1

turn = len(nums)

while turn < 2020:
	lastNum = nums[-1:][0]
	lastSaid = list_rindex(nums, lastNum)
	lastSaid2 = list_rindex(nums, lastNum, lastSaid)

	if lastSaid2 == -1:
		nums.append(0)
	else:
		nums.append(lastSaid - lastSaid2)

	turn += 1

print(nums)

print(nums[-1:][0])
