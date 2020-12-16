import copy

def validate_rule(val, rule):
	split = rule.split("-")
	if int(val) in range(int(split[0]), int(split[1]) + 1):
		return True
	return False

class TicketSet:
	def __init__(self, tickets, rules):
		self.rules = rules
		self.tickets = []
		for ticket in tickets:
			if self.is_valid(ticket.split(",")):
				self.tickets.append(ticket.split(","))

		self.emptyDef = []
		self.finalDef = []
		self.ruleDef = []
		for i in self.rules:
			self.emptyDef.append([])
			self.finalDef.append(None)
			self.ruleDef.append('')

		self.foundRules = []
		self.find_ticket_values()


	def is_valid(self, vals):
		for val in vals:
			found = False
			for rule in self.rules:
				for rng in rules[rule]:
					if validate_rule(val, rng):
						found = True
						break
				if found:
					break
			if not found:
				return False
		return True

	def rules_set(self):
		for rule in self.ruleDef:
			if not rule:
				return False
		return True



	def find_ticket_values(self):
		while len(self.foundRules) != len(rules):
			for ticket in self.tickets:
				ticketRules = self.ticket_rules(ticket)
				for num, rule in enumerate(self.ruleDef):
					if self.ruleDef[num] == '':
						self.ruleDef[num] = ticketRules[num]
					else:
						for val in self.ruleDef[num]:
							if not val in ticketRules[num]:
								self.ruleDef[num].remove(val)
					if len(self.ruleDef[num]) == 1 and not self.ruleDef[num][0] in self.foundRules:
						self.foundRules.append(self.ruleDef[num][0])
						self.finalDef[num] = self.ruleDef[num][0]


	def ticket_rules(self, ticket):
		result = copy.deepcopy(self.emptyDef)
		for num, val in enumerate(ticket):
			for rule in self.rules:
				if rule in self.foundRules:
					if self.finalDef[num] == rule:
						result[num].append(rule)
					continue
				for rng in rules[rule]:
					if validate_rule(val, rng):
						result[num].append(rule)
						break
		return result

def parse_rules(raw):
	result = {}
	for rule in raw:
		newRule = rule.split(": ")
		name = newRule[0]
		rng = newRule[1].split(" or ")
		result[name] = rng
	return result

inFile = open("day16.in", "r").read().split("\n\n")

rulesRaw = inFile[0].split("\n")
myTicket = inFile[1].split("\n")
myTicket.pop(0)
otherTickets = inFile[2].split("\n")
otherTickets.pop(0)
otherTickets.pop()

rules = parse_rules(rulesRaw)

validTickets = []

tickets = TicketSet(otherTickets + myTicket, rules)

result = 1

myTicket = myTicket[0].split(",")
for num, rule in enumerate(tickets.finalDef):
	splitRule = rule.split(" ")
	if splitRule[0] == 'departure':
		result *= int(myTicket[num])


print(result)
