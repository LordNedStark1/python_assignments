import random
arr_list =[]

count =10
index =0

while 0<count:
	val= arr_list.insert(index,count)
	index =index +1
	count =count -1

#for i in range(len(arr_list)):
#	print ("index --> ", i , "value--> ", arr_list[i])
#print("difference")

#arr_list.insert(5,"man")

#[print("index --> ",i , "value --> ", arr_list[i]) for i in rang e(len(arr_list))]
print (" random--> : ", random.choice(arr_list))

print('random--> ', random.choice(6))