def listAnd(list):
    stringToReturn = ''
    for i in range(0, len(list)):
        if i == len(list) - 1:
            stringToReturn = stringToReturn + ' and ' + str(list[i])
        elif i == 0:
            stringToReturn = str(list[i])
        else:
            stringToReturn = stringToReturn + ', ' + str(list[i])

    return stringToReturn

spam = ['apples', 'bananas', 'tofu', 41]

print(listAnd(spam))