import re

GALAXY_CENTER = 'COM'
GALAXY = {}

class ObjectMass:
	def __init__(self, objectName):
		self.objectName = objectName
		self.parentObject = ""
		self.childObjects = []

	def add_child_object(self, childObject):
		if not childObject in self.childObjects:
			self.childObjects.append(childObject)

	def set_parent_object(self, parentObject):
		self.parentObject = parentObject

	def count_indirect_orbits(self):
		if self.parentObject == GALAXY_CENTER:
			return 1

		return 1 + GALAXY[self.parentObject].count_indirect_orbits()

	def is_leaf(self):
		return len(self.childObjects) == 0

	def has_destination(self, destination):
		return destination in self.childObjects

	def find_destination(self, destination, checked = [], initial = 1, fromParent = False):
		if destination in self.childObjects:
			return 0
		if self.parentObject == GALAXY_CENTER:
			return 9999
		if self.objectName in checked:
			return 9999

		checked.append(self.objectName)

		best = 9999
		if not fromParent:
			best =  GALAXY[self.parentObject].find_destination(destination, checked, 0)

		for objectMass in self.childObjects:
			best = min(best, GALAXY[objectMass].find_destination(destination, checked, 0, True))

		if initial:
			return best
		else:
			return 1 + best


inFile = open("day-6.in", "r").read().split("\n")
inFile.pop()

for objectPair in inFile:
	m = re.search('([0-9a-zA-Z]+).([0-9a-zA-Z]+)', objectPair)
	parent = m.group(1)
	child = m.group(2)

	if not parent == GALAXY_CENTER and not parent in GALAXY:
		GALAXY[parent] = ObjectMass(parent)

	if not child in GALAXY:
		GALAXY[child] = ObjectMass(child)

	GALAXY[child].set_parent_object(parent)
	if not parent == GALAXY_CENTER:
		GALAXY[parent].add_child_object(child)

count = 0
for objectMass in GALAXY:
	count += GALAXY[objectMass].count_indirect_orbits()

print("Part 1: " + str(count))

print("Part 2: " + str(GALAXY['YOU'].find_destination('SAN')))

