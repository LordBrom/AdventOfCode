import re

# part 1

fields = [
	['byr', True],
	['iyr', True],
	['eyr', True],
	['hgt', True],
	['hcl', True],
	['ecl', True],
	['pid', True],
	['cid', False]
]

def check_passport(passport):
	splitPort = passport.split(" ")
	goodPassport = True
	for port in splitPort:
		part = port[:3]
		rest = port[4:]
		if part == 'cid':
			continue

		elif part == 'byr':
			if int(rest) < 1920 or int(rest) > 2002:
				goodPassport = False

		elif part == 'iyr':
			if int(rest) < 2010 or int(rest) > 2020:
				goodPassport = False

		elif part == 'eyr':
			if int(rest) < 2020 or int(rest) > 2030:
				goodPassport = False

		elif part == 'hgt':
			m = re.search('^([0-9]{2,3})(cm|in)$', rest)
			try:
				number = m.group(1)
				unit = m.group(2)
			except:
				goodPassport = False
				continue
			if unit == 'cm' and int(number) >= 150 and int(number) <= 193:
				pass
			elif unit == 'in' and int(number) >= 59 and int(number) <= 76:
				pass
			else:
				goodPassport = False

		elif part == 'hcl':
			if not re.search('^#[0-9a-f]{6}$', rest):
				goodPassport = False

		elif part == 'ecl':
			if not re.search('^(amb|blu|brn|gry|grn|hzl|oth)$', rest):
				goodPassport = False

		elif part == 'pid':
			if not re.search('^[0-9]{9}$', rest):
				goodPassport = False

	for f in fields:
		if not f[1]:
			continue
		elif passport.find(f[0] + ":") == -1:
			goodPassport = False

	return goodPassport

inFile = open("day4.in", "r").read().split("\n\n")
inFile.pop()

count = 0

for i in inFile:
	passport = i.replace("\n", " ")
	if check_passport(passport):
		count += 1


print(count)
