from intcode import IntcodeComputer

inFile = open("day2.in", "r").read().split(",")

inFile[1] = 12
inFile[2] = 2

comp = IntcodeComputer(inFile)
comp.run()

print(comp.get_intcode()[0])

