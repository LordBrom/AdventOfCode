import copy
inFile = open("day22.in", "r").read().split("\n\n")

deck1 = inFile[0][9:].strip().split("\n")
deck2 = inFile[1][9:].strip().split("\n")

deck1 = [int(x) for x in deck1]
deck2 = [int(x) for x in deck2]

class CrabCombat:
	def __init__(self, deck1, deck2, subGame = 0):
		self.deck1 = deck1
		self.deck2 = deck2
		self.winner = None
		self.winningDeck = None
		self.gameOver = False
		self.round = 0
		self.subGame = subGame

		self.history1 = []
		self.history2 = []

	def play_round(self):
		self.round += 1

		if self.deck1 in self.history1 or self.deck2 in self.history2:
			self.gameOver = 1
			self.winner = 1
			self.winningDeck = self.deck1
			return

		self.history1.append(copy.deepcopy(self.deck1))
		self.history2.append(copy.deepcopy(self.deck2))

		card1 = self.deck1.pop(0)
		card2 = self.deck2.pop(0)

		roundWinner = None

		if len(self.deck1) >= card1 and len(self.deck2) >= card2:
			newDeck1 = copy.deepcopy(self.deck1)[:card1]
			newDeck2 = copy.deepcopy(self.deck2)[:card2]
			roundWinner = self.run_sub_game(copy.deepcopy(newDeck1), copy.deepcopy(newDeck2))
		else:
			if card1 > card2:
				roundWinner = 1

			elif card1 < card2:
				roundWinner = 2

		if roundWinner == 1:
			self.deck1.append(card1)
			self.deck1.append(card2)
		elif roundWinner == 2:
			self.deck2.append(card2)
			self.deck2.append(card1)

		if len(self.deck1) == 0:
			self.winner = 2
			self.winningDeck = self.deck2
			self.gameOver = True
		elif len(self.deck2) == 0:
			self.winner = 1
			self.winningDeck = self.deck1
			self.gameOver = True

	def run_sub_game(self, new1, new2):
		subCombat = CrabCombat(new1, new2, self.subGame + 1)

		while not subCombat.gameOver:
			subCombat.play_round()

		return subCombat.winner

combat = CrabCombat(deck1, deck2)

while not combat.gameOver:
	combat.play_round()

winningDeck = combat.winningDeck
winningDeck.reverse()

score = 0
for n, i in enumerate(winningDeck):
	score += (n + 1) * (i)

print(score)
