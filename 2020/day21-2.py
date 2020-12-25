ALL_ALLERGENS = {}
ALL_INGREDIENTS = {}
INGREDIENT_ALLERGENS = {}
FOUND_ALLERGENS = []
FOUND_INGREDIENT = []

class Food:
	def __init__(self, inStr, foodRow):
		splitStr = inStr.split(" (contains ")
		self.ingredients = splitStr[0].split(" ")
		for ing in self.ingredients:
			if not ing in ALL_INGREDIENTS:
				ALL_INGREDIENTS[ing] = 0
			ALL_INGREDIENTS[ing] += 1
		self.allergens = splitStr[1].split(" ")

		for num, allergen in enumerate(self.allergens):
			self.allergens[num] = allergen[:-1]

		for num, allergen in enumerate(self.allergens):
			if allergen in FOUND_ALLERGENS:
				continue
			if not allergen in ALL_ALLERGENS:
				ALL_ALLERGENS[allergen] = self.ingredients
			else:
				ALL_ALLERGENS[allergen] = [x for x in ALL_ALLERGENS[allergen] if x in self.ingredients]
				if len(ALL_ALLERGENS[allergen]) == 1:
					FOUND_ALLERGENS.append(allergen)
					FOUND_INGREDIENT.append(ALL_ALLERGENS[allergen][0])
					INGREDIENT_ALLERGENS[ALL_ALLERGENS[allergen][0]] = allergen


inFile = open("day21.in", "r").read().split("\n")
inFile.pop()

foods = []

for num, i in enumerate(inFile):
	foods.append(Food(i, num))

while len(FOUND_ALLERGENS) < len(ALL_ALLERGENS):
	for allergen in ALL_ALLERGENS:
		if not allergen in FOUND_ALLERGENS:
			ALL_ALLERGENS[allergen] = [x for x in ALL_ALLERGENS[allergen] if x not in FOUND_INGREDIENT]
			if len(ALL_ALLERGENS[allergen]) == 1:
				FOUND_ALLERGENS.append(allergen)
				FOUND_INGREDIENT.append(ALL_ALLERGENS[allergen][0])
				INGREDIENT_ALLERGENS[ALL_ALLERGENS[allergen][0]] = allergen

mapping = {}

for n,a in enumerate(FOUND_ALLERGENS):
	mapping[a] = FOUND_INGREDIENT[n]

print(','.join(mapping[x] for x in sorted(FOUND_ALLERGENS)))
