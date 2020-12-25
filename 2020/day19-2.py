import re

def buildStr(r, rules):
	result = ""
	curRules = rules[r]
	if isinstance(curRules, list):
		firstSet = True
		result += "("
		repeat = ""
		for ruleSet in curRules:
			if not firstSet:
				result += "|"
			for rule in ruleSet:
				result += buildStr(rule, rules)
			firstSet = False
		result += ")" + repeat
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


new8 = "42 | 42 8"
new11 = "42 31 | 42 11 31"

ruleOr = new8.split("|")
rules['8'] = []
for rule in ruleOr:
	rules['8'].append(rule.strip().split(" "))

ruleOr = new11.split("|")
rules['11'] = []
for rule in ruleOr:
	rules['11'].append(rule.strip().split(" "))

regStr42 = buildStr('42', rules)
regStr31 = buildStr('31', rules)

regStr = "(" + regStr42 + ")+(" + regStr31 + ")+"

count = 0
for m in messages:

	if re.match("^" + regStr + "$", m):
		s42 = re.search("^(" + regStr42 + ")+", m)
		s31 = re.search("(" + regStr31 + ")+$", m)
		count42 = len(re.findall(regStr42, s42.group()))
		count31 = len(re.findall(regStr31, s31.group()))
		if count42 > count31:
			count += 1

print(count)
