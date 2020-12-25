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

slope = open("day3.in", "r").read().split("\n")
slope.pop()

count = find_trees(slope, 3, 1)

print(count)
