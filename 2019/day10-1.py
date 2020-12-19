import math

def calc_angle(p1, p2):
	deltaX = p1[0] - p2[0]
	deltaY = p1[1] - p2[1]
	return math.atan2(deltaX, deltaY) / math.pi

def count_visible(asteroids, current):
	foundAngles = []
	for asteroid in asteroids:
		if asteroid == current:
			continue
		angle = calc_angle(current, asteroid)
		if not angle in foundAngles:
			foundAngles.append(angle)
	return foundAngles

inFile = open("day10.in", "r").read().split("\n")

asteroids = []

for row in enumerate(inFile):
	for col in enumerate(row[1]):
		if inFile[row[0]][col[0]] == '#':
			asteroids.append([row[0], col[0]])

result = 0
for asteroid in asteroids:
	result = max(result, len(count_visible(asteroids, asteroid)))

print(result)

