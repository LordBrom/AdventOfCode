inputsArray = open("day1.in", "r").read().split("\n")
inputsArray.pop()

for i in range(len(inputsArray)):
	for j in range(i, len(inputsArray)):
		for k in range(j, len(inputsArray)):
			if int(inputsArray[i]) + int(inputsArray[j]) + int(inputsArray[k]) == 2020:
				print(int(inputsArray[i]) * int(inputsArray[j]) * int(inputsArray[k]))
