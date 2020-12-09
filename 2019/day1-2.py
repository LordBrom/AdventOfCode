from math import floor

def calc_fuel(mass):
	step1 = floor(int(mass) / 3)
	step2 = max(step1 - 2, 0)
	if step2 > 0:
		return step2 + calc_fuel(step2)
	return step2

total = 0

inFile = open("day1.in", "r").read().split("\n")
inFile.pop()

for num in inFile:
	total += calc_fuel(num)

print(total)


