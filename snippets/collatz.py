valueInput = ''

def collatz(number):
    if number % 2 == 0:
        value = number // 2
        print(value)
        return value
    else:
        value = 3 * number + 1
        print(value)
        return value

print('Enter an integer')

while valueInput == '':
    try:
        valueInput = int(input())
    except ValueError:
        print('Error: not an int, try again!')

while valueInput != 1:
    valueInput = collatz(valueInput)
