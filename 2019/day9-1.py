
from intcode import IntcodeComputer





inFile = open("day9.in", "r").read().split(",")

comp = IntcodeComputer(inFile, True)
print(comp.run())
#lastOutput = comp.run(lastOutput)
