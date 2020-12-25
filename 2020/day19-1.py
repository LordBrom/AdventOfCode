import re

def buildStr(r, rules):
	result = ""
	curRules = rules[r]
	if isinstance(curRules, list):
		firstSet = True
		result += "("
		for ruleSet in curRules:
			if not firstSet:
				result += "|"
			for rule in ruleSet:
				result += buildStr(rule, rules)
			firstSet = False
		result += ")"
	else:
		return curRules

	return result

inFile = open("day19.in", "r").read().split("\n\n")
rulesRaw = inFile[0]
messages = inFile[1].split("\n")
messages.pop()

rf = re.findall("([0-9]+): ([a-z0-9|\" ]+)", rulesRaw)

rules = {}

for r in rf:
	ind = r[0]
	if r[1].find('"') == -1:
		ruleOr = r[1].split("|")
		rules[ind] = []
		for rule in ruleOr:
			rules[ind].append(rule.strip().split(" "))
	else:
		rules[ind] = r[1].replace('"', "")

count = 0

regStr = buildStr('0', rules)[1:-1]
regStr = regStr.replace(")|(", "))|((")

for m in messages:
	if re.match("^" + regStr + "$", m):
		count += 1

print(count)
