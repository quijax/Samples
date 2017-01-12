import random

def randpixel(color1,color2,percentage=50):
	"""Chooses between two different colors. If percentage is specified, 
	weight is applied to color1. That is, if you want color1 to be chosen 60%
	of the time, percentage should be 60."""
	random.seed()
	if random.randint(0,100) >= percentage:
		color = color2
	else:
		color = color1
	return color