import re

def is_valid_password(input):
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
inputText = open("day2.in", "r").read().split("\n")
inputText.pop()
for text in inputText:
	if is_valid_password(text):
		count += 1

print(count)
