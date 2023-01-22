#print ("i "," i^2 ", " i^3")
#for i in range(11): print (i, "  ",i**2,"  ", i**3)

#for i in range(5): print("welcome to python")

#print( (9.5*4.5-2.5*3)/(45.5-3.5))

#width=float( input( "Enter the width : "))
#height=float(input( "Enter the height: "))

#area =width *height
#print (f"\nThe height is: {height} ,\
#	\nwidth is: {width},\
#	 \nThe area is:  { area}")

#for i in range(1, 11, 1): print(i)
# for i in range(10, 0, -1): print(i)

#for i in range(1,11): print(i)
#for i in range(11,2, -1): i=11
#print(i)

#arr = [2,3,6,7,8,9]
#for i in range (0, len(arr),+2):
#	print("Index ={}, value ={}".format(i,arr[i]))

#for i in range (len(arr)-1,1,-1):
#	print("Index ={}, value ={}".format(i,arr[i]))

#i=1
#for i in range(0 , len(arr), i *2):
#	print("Index ={}, value ={}".format(i,arr[i]))

#sum=0
#for i in range( len(arr)):
#	sum +=arr[i]
#print("the sum is: ", sum)

#for i in range(5):
#	num= int(input("Enter a number to sum"))
#	sum +=num 
#print("The sum is : ", sum)

#for i in range(len(arr)-1,-1, -1):
#	print(arr[i])

man=[]
a_string = "my name is wonder"
#for i in a_string:
#	print(i)
#print(man.append(a_string))
s= a_string.split(" ")	
print(s)
#for i in range(len(s)):
#	print (s[i])
#	for j in s[i]:
#	    print(j)
#print (a_string)

for index, value in enumerate(s):
	print("index = ", index,"value= ",value)

print("next")

for index, value in enumerate(a_string):
	print("index = ", index,"value= ",value)