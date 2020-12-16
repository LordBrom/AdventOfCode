

def parse_rules(raw):
	result = {}
	for rule in raw:
		newRule = rule.split(": ")
		name = newRule[0]
		rng = newRule[1].split(" or ")
		result[name] = rng
	return result

def validate_ticket(ticket, rules = []):
	badVal = []
	for val in ticket:
		found = False
		for rule in rules:
			for rng in rules[rule]:
				split = rng.split("-")
				if int(val) in range(int(split[0]), int(split[1]) + 1):
					found = True
					break
			if found:
				break
		if not found:
			badVal.append(int(val))
	return badVal

inFile = open("day16.in", "r").read().split("\n\n")

rulesRaw = inFile[0].split("\n")
myTicket = inFile[1].split("\n")
myTicket.pop(0)
otherTickets = inFile[2].split("\n")
otherTickets.pop(0)
otherTickets.pop()

rules = parse_rules(rulesRaw)

count = 0
for ticket in otherTickets:
	for badVal in validate_ticket(ticket.split(","), rules):
		count += badVal

print(count)
