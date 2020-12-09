import re

IMAGE_WIDTH = 25
IMAGE_HEIGHT = 6
LAYER_SIZE = IMAGE_WIDTH * IMAGE_HEIGHT

inFile = open("day8.in", "r").read()
reFind = re.findall(".{" + str(LAYER_SIZE) + "}", inFile)

result = ''

for i in range(LAYER_SIZE):
	pixelFound = False
	for j in range(len(reFind)):
		if reFind[j][i] != '2':
			if reFind[j][i] == '0':
				result += " "
			else:
				result += "1"
			pixelFound = True
			break

	if not pixelFound:
		result += " "

match = re.findall(".{" + str(IMAGE_WIDTH) + "}", result)
for out in match:
	print(out)
