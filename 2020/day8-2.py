def run_startup(code):

	accumulator = 0
	pointer = 0

	run = True
	check = []
	for i in code:
		check.append(False)
	while run:
		if pointer >= len(inFile):
			return accumulator
		if check[pointer]:
			break
		check[pointer] = True
		if code[pointer][0] == 'acc':
			accumulator += int(code[pointer][1])
			pointer += 1
		elif code[pointer][0] == 'jmp':
			pointer += int(code[pointer][1])
		elif code[pointer][0] == 'nop':
			pointer += 1

	return ""

inFile = open("day8.in", "r").read().split("\n")
inFile.pop()

for i in range(len(inFile)):
	inFile[i] =  inFile[i].split(" ")

result = 0
for i in range(len(inFile)):

	if inFile[i][0] == "jmp":
		inFile[i][0] = "nop"
		output = run_startup(inFile)
		if output != "":
			result = output
		inFile[i][0] = "jmp"

	elif inFile[i][0] == "nop":
		inFile[i][0] = "jmp"
		output = run_startup(inFile)
		if output != "":
			result = output
		inFile[i][0] = "nop"

print(result)
