# input: 273025-767253

def check_valid(num):
	#Rule 1: It is a six-digit number.
	if len(num) != 6:
		return False

	#Rule 2: The value is within the range given in your puzzle input. - given
	#Rule 3: Two adjacent digits are the same (like 22 in 122345).
	#Part 2: the two adjacent matching digits are not part of a larger group of matching digits.
	digitCount = [0, 0, 0, 0, 0, 0, 0, 0, 0]
	doubleCount = 0
	for i in range(6):
		digitCount[int(num[i]) - 1] += 1
		if digitCount[int(num[i]) - 1] == 2:
			doubleCount += 1
		elif digitCount[int(num[i]) - 1] == 3: #Part 2
			doubleCount -= 1

	if doubleCount == 0:
		return False

	#Rule 4: Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
	if ''.join(sorted(num)) != num:
		return False
	return True

print('112233: ' + str(check_valid('112233')))
print('123444: ' + str(check_valid('123444')))
print('111122: ' + str(check_valid('111122')))

inpRange = input("input range: ")

minRange = inpRange[:6]
maxRange = inpRange[7:]

count = 0
for i in range(int(minRange), int(maxRange)):
	if check_valid(str(i)):
		count += 1
		#print(i)

#print("=======")
print(count)
