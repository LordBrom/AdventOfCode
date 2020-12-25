inputsArray = open("day1.in", "r").read().split("\n")
inputsArray.pop()

for i in range(len(inputsArray)):
	for j in range(i, len(inputsArray)):
		if int(inputsArray[i]) + int(inputsArray[j]) == 2020:
			print("Part 1: " + str(int(inputsArray[i]) * int(inputsArray[j])))
		for k in range(j, len(inputsArray)):
			if int(inputsArray[i]) + int(inputsArray[j]) + int(inputsArray[k]) == 2020:
				print("Part 2: " + str(int(inputsArray[i]) * int(inputsArray[j]) * int(inputsArray[k])))
