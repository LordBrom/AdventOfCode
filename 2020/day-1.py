inputsArray = []
inputText = input("Input: ")
while inputText != '':
	inputsArray.append(int(inputText))
	inputText = input("Input: ")

for i in range(len(inputsArray)):
	for j in range(i, len(inputsArray)):
		for k in range(j, len(inputsArray)):
			if inputsArray[i] + inputsArray[j] + inputsArray[k] == 2020:
				print(inputsArray[i])
				print(inputsArray[j])
				print(inputsArray[k])
				print(inputsArray[i] * inputsArray[j] * inputsArray[k])

#print(do_something(inputText))

