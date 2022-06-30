from itertools import count
import random
numberOfStreaks = 0
numberOfCoinflips = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coinFlipList = []
    for coinFlips in range (100):
        numberOfCoinflips += 1
        if random.randint(0, 1) == 0:
            coinFlipList.append("H")
        else:
            coinFlipList.append("T")

    lastCoin = ''
    streak = 0
    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(len(coinFlipList)):
        currentCoin = coinFlipList[i]
        if streak == 5:
            numberOfStreaks += 1
            streak = 0

        if currentCoin == "H" and currentCoin == lastCoin:
            streak += 1
        else:
            streak = 0

        lastCoin = coinFlipList[i]
    

print('Chance of streak: %s%%' % (numberOfStreaks / 10000))
print(numberOfStreaks)
print(numberOfCoinflips)