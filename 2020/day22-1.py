inFile = open("day22.in", "r").read().split("\n\n")

deck1 = inFile[0][9:].strip().split("\n")
deck2 = inFile[1][9:].strip().split("\n")

deck1 = [int(x) for x in deck1]
deck2 = [int(x) for x in deck2]

class CrabCombat:
	def __init__(self, deck1, deck2):
		self.deck1 = deck1
		self.deck2 = deck2
		self.winningDeck = None
		self.gameOver = False
		self.round = 0

	def play_round(self):
		self.round += 1
		card1 = self.deck1.pop(0)
		card2 = self.deck2.pop(0)

		if card1 > card2:
			self.deck1.append(card1)
			self.deck1.append(card2)

		elif card1 < card2:
			self.deck2.append(card2)
			self.deck2.append(card1)

		if len(deck1) == 0:
			self.winningDeck = self.deck2
			self.gameOver = True
		elif len(deck2) == 0:
			self.winningDeck = self.deck1
			self.gameOver = True

combat = CrabCombat(deck1, deck2)

while not combat.gameOver:
	combat.play_round()

winningDeck = combat.winningDeck
winningDeck.reverse()

score = 0
for n, i in enumerate(winningDeck):
	score += (n + 1) * (i)

print(score)
