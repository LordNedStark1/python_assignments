import random
option= int(input("1-->to play "))

while	option == 1:

	first =random.randint(0,9)
	second =random.randint(0,9)
	answer = int(input(f"what is { first} + {second} =" ))
	sum = first +second

	if answer == sum:
		print("correct!")
	else:
		print("wrong, try next question")
	
	option= int(input("1-->to play"))
