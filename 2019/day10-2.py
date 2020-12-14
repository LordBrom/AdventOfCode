import math

def calc_angle(p1, p2):
	deltaX = p1[0] - p2[0]
	deltaY = p1[1] - p2[1]
	angle = math.atan2(deltaX, deltaY) / math.pi

	angle = angle - 0.5

	if angle >= 0:
		return angle
	else:
		return (2 + angle)

def calc_dist(p1,p2):
	deltaX = p1[0] - p2[0]
	deltaY = p1[1] - p2[1]

	dist = math.sqrt((deltaX)**2 + (deltaY)**2)

	return dist

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
bestAsteroid = None
for asteroid in asteroids:
	newResult = len(count_visible(asteroids, asteroid))
	if newResult > result:
		result = newResult
		bestAsteroid = asteroid

angles = []
asteroidAngles = {}

for asteroid in asteroids:
	if asteroid == bestAsteroid:
		continue
	angle = calc_angle(bestAsteroid, asteroid)
	if not angle in angles:
		angles.append(angle)
		asteroidAngles[angle] = []
	asteroidAngles[angle].append([asteroid, calc_dist(bestAsteroid, asteroid)])

angles.sort()
for asteroidAngle in asteroidAngles:
	asteroids = asteroidAngles[asteroidAngle]
	asteroidAngles[asteroidAngle] = sorted(asteroids, key=lambda x: x[1])

findCount = 200
result = None

count = 0
pointer = 0
while True:
	count += 1
	curAngle = angles[pointer]
	asteroid = asteroidAngles[curAngle].pop(0)
	#print("The", count, "asteroid to be vaporized is at", asteroid[0], "at angle", curAngle, "and distance", asteroid[1])
	print("The", count, "asteroid to be vaporized is at", asteroid[0])
	if count == findCount:
		result = asteroid[0]
	if len(asteroidAngles[curAngle]) == 0:
		angles.pop(pointer)
		if len(angles) == 0:
			break
		pointer = pointer % len(angles)
	else:
		pointer += 1
		pointer = pointer % len(angles)

if result:
	print((result[1] * 100) + result[0])

