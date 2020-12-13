import itertools

from intcode import IntcodeComputer

inFile = open("day7.in", "r").read().split(",")

lastOutput = 0
maxOutput = 0
for pattern in itertools.permutations(range(5), 5):
	lastOutput = 0
	for i in pattern:
		comp = IntcodeComputer(inFile)
		comp.run(i)
		lastOutput = comp.run(lastOutput)
	maxOutput = max(maxOutput, lastOutput)

print(maxOutput)
