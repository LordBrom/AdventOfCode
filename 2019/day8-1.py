import re

IMAGE_WIDTH = 25
IMAGE_HEIGHT = 6

LAYER_SIZE = IMAGE_WIDTH * IMAGE_HEIGHT

IMAGE = []

inFile = open("day8.in", "r").read()

reFind = re.findall(".{" + str(LAYER_SIZE) + "}", inFile)

min0 = -1

result = 0

for i in reFind:
	find0 = re.findall("0", i)
	find1 = re.findall("1", i)
	find2 = re.findall("2", i)

	if min0 > len(find0) or min0 == -1:
		min0 = len(find0)
		result = len(find1) * len(find2)

print(result)
