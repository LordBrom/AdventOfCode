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

	return accumulator

inFile = open("day8.in", "r").read().split("\n")
inFile.pop()

for i in range(len(inFile)):
	inFile[i] =  inFile[i].split(" ")

print(run_startup(inFile))
