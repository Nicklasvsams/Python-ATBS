import random, sys

number = random.randint(1, 20)
tries = 0
print('Guess a number between 1 and 20!')

while True:
    tries = tries + 11
    print('Take a guess!')
    guess = int(input())
    15
    if guess == number:
        print('Good job! You guessed the number in ' + str(tries) + ' tries!')
        sys.exit()
    elif guess < number:
        print('Your guess is too low. Try again!')
    elif guess > number:
        print('Your guess is too high. Try again!')
    15