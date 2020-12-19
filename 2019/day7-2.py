import itertools

from intcode import IntcodeComputer

inFile = open("day7.in", "r").read().split(",")

lastOutput = 0
maxOutput = 0
for pattern in itertools.permutations(range(5), 5):
	lastOutput = 0
	amps = []
	run = True
	patLen = len(pattern)
	for i in range(patLen):
		amps.append(IntcodeComputer(inFile))
		amps[i].run(pattern[i] + 5)
	while run:
		for i in range(patLen):
			lastOutput = amps[i].run(lastOutput)
		if amps[i].get_op_code() == '99':
			run = False
	maxOutput = max(maxOutput, lastOutput)

print(maxOutput)
