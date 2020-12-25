import re

def is_valid_password(input):
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

count = 0
inputText = open("day2.in", "r").read().split("\n")
inputText.pop()
for text in inputText:
	if is_valid_password(text):
		count += 1

print(count)
