
word = 'LifeIsGood'
word_two = 'yesterdayYouWentHomeTodayYouWillNotGoHome'

def word_count(words):
    alhabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    count = 0
    if words[0].islower():
        count += 1
    for i in range(len(words)):
        for j in range(len(alhabets)):
            if words[i] == alhabets[j]:
                count += 1
    return count

print(word_count(word_two))
