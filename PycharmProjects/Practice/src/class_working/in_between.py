

def in_between(array):
    newArray = []
    for i in range( 1 , len(array), +2):
        newArray.append(array[i])

    return newArray

arr = [1,2,3,4,5,6]
print(in_between(arr))