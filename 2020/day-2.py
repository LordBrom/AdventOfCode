import re

def is_valid_password_part_2(input):
	m = re.search('([0-9]+)-([0-9]+) ([a-z]+): ([a-z]+)', input)
	minRange = m.group(1)
	maxRange = m.group(2)
	letter   = m.group(3)
	password = m.group(4)

	letterCount = 0

	if password[int(minRange) - 1] == letter:
		letterCount += 1

	if password[int(maxRange) - 1] == letter:
		letterCount += 1

	return letterCount == 1

def is_valid_password_part_1(input):
	m = re.search('([0-9]+)-([0-9]+) ([a-z]+): ([a-z]+)', input)
	minRange = m.group(1)
	maxRange = m.group(2)
	letter   = m.group(3)
	password = m.group(4)

	letterCount = 0
	for i in password:
		if i == letter:
			letterCount += 1
	if letterCount >= int(minRange) and letterCount <= int(maxRange):
		return True
	return False

count1 = 0
count2 = 0
inputText = open("day-2.in", "r").read().split("\n")
inputText.pop()
for text in inputText:
	if is_valid_password_part_1(text):
		count1 += 1
	if is_valid_password_part_2(text):
		count2 += 1

print("part 1:" + str(count1))
print("part 2:" + str(count2))
