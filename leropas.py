import random
pScore = 0
bScore = 0
play = True
textData = ""
def botWins():
	global bScore, pScore
	bScore += 1
	print("Bot: " + str(bScore) + " Player: " + str(pScore))
def playerWins():
	global bScore, pScore
	pScore += 1
	print("Bot: " + str(bScore) + " Player: " + str(pScore))
def draw():
	global bScore, pScore
	print("Bot: " + str(bScore) + " Player: " + str(pScore))
dict = {
	"RR" : lambda: draw(),
	"RS" : lambda: playerWins(),
	"RP" : lambda: botWins(),
	"SS" : lambda: draw(),
	"SP" : lambda: playerWins(),
	"SR" : lambda: botWins(),
	"PP" : lambda: draw(),
	"PR" : lambda: playerWins(),
	"PS" : lambda: botWins(),
}
while play == True:
	print("\n Rock, paper or scissors? R for rock, P for paper, S for scissors")
	playerSelection = input().upper()
	if(playerSelection == 'R' or 'S' or 'P'):
		if len(textData) == 4:
			textData = textData[1 : ]
		textData += playerSelection
		if(textData.count('R')*25 >= random.randint(0, 100)):
			botChoice = 'P'
			print("I play paper")
			dictElement = playerSelection + botChoice
			dict[dictElement]()
		elif(textData.count('S')*25 >= random.randint(0, 100)):
			print("I play rock")
			botChoice = 'R'
			dictElement = playerSelection + botChoice
			dict[dictElement]()
		elif(textData.count('P')*25 >= random.randint(0, 100)):
			print("I play scissors")
			botChoice = 'S'
			dictElement = playerSelection + botChoice
			dict[dictElement]()
		else:
			list = ['scissors', 'paper', 'rock']
			choice = random.choice(list)
			print("I play " + choice )
			botChoice = str(choice[0]).upper()
			dictElement = playerSelection + botChoice
			dict[dictElement]()
