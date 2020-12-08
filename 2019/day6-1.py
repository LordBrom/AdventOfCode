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


inFile = open("day6.in", "r").read().split("\n")
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

print(count)


