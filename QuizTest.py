#prompt the user to use the app
# ask question, collect the answer from user.
#evaluate the question and determine if the user is right


print("Welcome to random quiz game\n")

option = input("Enter yes to start no to end ")
while	option == "yes":
	
	question_one =input("\nIs water transparent, yes/ no / maybe ")

	if question_one == "yes":
		print("correct")
	elif question_one == "no":
		print("not true, try another question")
	else:
		print("coordinate your thoughts")

	question_two = eval(input("what is the value of 2 * 4 "))

	if question_two == 8:
		print("correct!")
	else:
		print("wrong")

	question_one =input("Is water wet yes/ no / maybe ")

	if question_one == "yes":
		print("correct")
	elif question_one == "no":
		print("not true, try another question")
	else:
		print("simple question you  can't answer")
	option = input("Enter yes to start no to end ")
 


if	option == "no":
	print ("oh no! come back soon")
else: 
	print("pick a valid option")