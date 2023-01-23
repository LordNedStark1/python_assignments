import random

quiz_questions =[]

quiz_questions.append("1. what is my name, ? a. ned b. head " )
quiz_questions.append("2. what is python (a) snake (b) laguage (c) a but b ")
quiz_questions.append("3. what state is semicolon in a. lagos b. house ")
quiz_questions.append("4. what is the colour of black a. green b. black ")
quiz_questions.append("5. what does love mean a. hate b. love ")
quiz_questions.append("6. what is voting a. to dance b. to vote ")
quiz_questions.append("7. java or python a. java b. python ")
quiz_questions.append("8. what is rain a. water b. fire ")
quiz_questions.append("9. man is a__ a. goat b. human ")
quiz_questions.append("10. light is__? a. bright b. black ")
quiz_questions.append("11. solar deals with a. dog b. sun ")
quiz_questions.append("12. is java sweet a. yes b. no ")
quiz_questions.append("13. snow is what colour a. green b. white ")
quiz_questions.append("14. is water wet a. no b. yes ")
quiz_questions.append("15. is love blind a. yes b. you go see ")
quiz_questions.append("16. String is what a. string b. word(s)")
quiz_questions.append("17. is food important a. no b. yes ")
quiz_questions.append("18. when should we breath\
  a. once in a while b. no need self c.always ")
quiz_questions.append("19. is quiz important \
	a. don't do it first b. maybe ")
quiz_questions.append("20. who  is Chibuzo a. b. c. chose wisely ")

quiz_answers =["a","c","a","b","b","b", "a","a","b","a","b","a","b","b","b","c","b","c","a","c"]
random_arr_selection=[]

user_choice= input("Do you want to take quiz ")

while (user_choice.lower() == "yes"):
  for i in range(20):
      random_arr_selection.append(21)
  correct =0
  incorrect =0
  option =int(input("1--> sequential questions,\n2--> random \n"))
  
   
  if option == 1:
    for i in range(len(quiz_questions)):
       print(quiz_questions[i])
       answer = input()
       if answer == quiz_answers[i]:
          correct+=1
       else:
          incorrect+=1 

  elif option ==2:
     for i in range (100):
       index = random.randint(0,19)

       if random_arr_selection[index]==21:
         random_arr_selection[index]=100
         
         print(quiz_questions[index])
         answer = input()
         if answer == quiz_answers[index]:
           correct+=1
         else:
            incorrect+=1 
      
  else:
     print("invalid option")

  if (correct >= 10)
    print("Brilliant!! You passed")
  else:
    print("I guess you should take the test again. and this time try harder")
  print ("the total correct is: ", correct)
  print ("the total incorrect is: ", incorrect)   
  random_arr_selection.clear()

  user_choice= input("Do you want to take quiz ")

print("thank you")