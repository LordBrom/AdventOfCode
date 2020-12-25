
def count_group_part1(group):
	found = []
	count = 0
	for person in group:
		for question in person:
			if not question in found:
				count += 1
				found.append(question)

	return count

def count_group_part2(group):
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
	total += count_group_part2(splitGroup)

print(total)
