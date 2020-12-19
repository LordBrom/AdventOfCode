from intcode import IntcodeComputer

inFile = open("day5.in", "r").read().split(",")
comp = IntcodeComputer(inFile)
print(comp.run(1))

