count= 1
sum = 0

#while (count<=10):
#	value= int(input("Enter a number to add: "))
#	sum += value 
#	count+=1
# print (sum)

arr= []
while (count <5):
	arr.append(input("enter a value"))
	count +=1
#print (arr)

#val =[x for x in range(len(arr))]
#print("arr -->", val)

for i in arr: sum+= arr[i]
print ("the sum of the array is:  ",sum)
