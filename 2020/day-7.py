import re

MY_BAG = "shiny gold"
BAG_RULES = {}

def find_bag(bag):
	found = False
	for subBag in BAG_RULES[bag]:
		if subBag["color"] == MY_BAG:
			found = True
		if find_bag(subBag["color"]):
			found = True
	return found

def count_bag(bag):
	count = 0
	for subBag in BAG_RULES[bag]:
		count += subBag["count"]
		count += count_bag(subBag["color"]) * subBag["count"]
	return count

def parse_rules(ruleFile):
	result = {}
	for rule in ruleFile:
		m = re.search('([a-z ]+) bags contain ([a-z0-9,. ]+)', rule)
		bagColor = m.group(1)
		rules = m.group(2)
		result[bagColor] = []
		m2 = re.findall('([0-9]+) ([a-z ]+) bag(|s)(,|.)', rules)
		for i in m2:
			result[bagColor].append({"color": i[1], "count": int(i[0])})
	return result


inFile = open("day-7.in", "r").read().split("\n")
inFile.pop()

BAG_RULES = parse_rules(inFile)

count = 0
for bag in BAG_RULES:
	if find_bag(bag):
		count += 1

print("Part 1: " + str(count))
print("Part 2: " + str(count_bag(MY_BAG)))
