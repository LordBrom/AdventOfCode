def find_trees(slope, rightMove, downMove):
	count = 0
	right = 0
	down = 0
	while down < len(slope):
		if slope[down][right] == "#":
			count += 1

		right += rightMove
		right = right % len(slope[0])
		down += downMove
	return count

slope = open("day-3.in", "r").read().split("\n")
slope.pop()

count1 = find_trees(slope, 1, 1)
count2 = find_trees(slope, 3, 1)
count3 = find_trees(slope, 5, 1)
count4 = find_trees(slope, 7, 1)
count5 = find_trees(slope, 1, 2)

print("part 1: " + str(count2))
print("part 2: " + str(count1 * count2 * count3 * count4 * count5))
