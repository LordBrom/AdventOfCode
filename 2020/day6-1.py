def count_group(group):
	found = []
	count = 0
	for person in group:
		for question in person:
			if not question in found:
				count += 1
				found.append(question)

	return count

inFile = open("day6.in", "r").read().split("\n\n")
inFile.pop()

total = 0

for group in inFile:
	splitGroup = group.split("\n")
	total += count_group(splitGroup)

print(total)
