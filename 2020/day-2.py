def is_valid_password_part_2(input):
	splitPos = input.index(":")

	rules = input[:splitPos]
	rulesSplitPos = rules.index(" ")
	rangeStr = rules[:rulesSplitPos]
	dashSplitPos = rangeStr.index("-")

	minRange = rangeStr[:dashSplitPos]
	maxRange = rangeStr[dashSplitPos + 1:]
	letter = rules[rulesSplitPos + 1:]
	password = input[splitPos + 2:]
	letterCount = 0

	if password[int(minRange) - 1] == letter:
		letterCount += 1

	if password[int(maxRange) - 1] == letter:
		letterCount += 1

	return letterCount == 1


def is_valid_password_part_1(input):
	splitPos = input.index(":")

	rules = input[:splitPos]
	rulesSplitPos = rules.index(" ")
	rangeStr = rules[:rulesSplitPos]
	dashSplitPos = rangeStr.index("-")

	minRange = rangeStr[:dashSplitPos]
	maxRange = rangeStr[dashSplitPos + 1:]
	letter = rules[rulesSplitPos + 1:]
	password = input[splitPos + 2:]
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
