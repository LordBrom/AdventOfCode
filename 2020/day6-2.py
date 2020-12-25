def count_group(group):
	found = []
	first = True
	for person in group:
		check = []
		for question in person:
			check.append(question)
		newFound = []
		if first:
			newFound = check
			first = False
		else:
			for q in found:
				if q in check:
					newFound.append(q)

		found = newFound

	return len(found)

inFile = open("day6.in", "r").read().split("\n\n")
inFile.pop()

total = 0

for group in inFile:
	splitGroup = group.split("\n")
	total += count_group(splitGroup)

print(total)
