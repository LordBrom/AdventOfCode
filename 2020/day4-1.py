import re

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
	goodPassport = True

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
