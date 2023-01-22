
seat_number= [ ]
option= int(input("Enter 1 to select seats"))

while (option==1):
	class_option = int(input("1--> first class\n"
			"2-->second class: \n"))	
	
	if (class_option== 1):
		
		seat_selection_option= int(input("1-->to select seat\n"
				"2-->to be given a seat:\n "))
		if(seat_selection_option==1):
			seat_number.append(int(input("Enter your seat number of choice: \n")))
			
			#for i in range (len(seat_number)):
			print(seat_number)
				
	option= int(input("Enter 1 to select seats"))