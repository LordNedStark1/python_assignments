

def noDuplicate(arr):
    newArr = []
    isTrue = False
    newArr.append(arr[0])
    for i in range(len(arr)):
        isTrue = False
        for j in range (len(newArr)):
            if arr[i] == newArr[j]:
                isTrue = False
                break
            elif arr[i] != newArr[j]:
                isTrue = True

        if (isTrue): newArr.append(arr[i])

    return newArr

def removeDuplicate(arr):
    tup = (arr[0])
    for i in range (len(arr)):
        tup = tup + (arr[i],)
    return tup



# question = [2,3,3,4,1,1,12,4]
# print(removeDuplicate(question))
tup = (1,2,4,5,1)
print(tup)