import random

def roll(sides=6):
	num_rolled = random.randint(1, sides)
	return num_rolled

def main():
	sides = 6
	rolling = True
	while rollling:
		rolling_dice = input("You ready? Enter=Roll. Q=Quit")
		if rolling_dice.upper() !="Q":
			num_rolled = roll(sides)
			print('You Rolled a', num_rolled)
		else:
			rolling = False
	print("Thanks for playing")
	