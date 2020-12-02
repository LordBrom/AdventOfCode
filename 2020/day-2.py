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

count = 0
inputText = input("Input: ")
while inputText != '':
	if is_valid_password_part_2(inputText):
		count += 1
	inputText = input("Input: ")

print(count)
