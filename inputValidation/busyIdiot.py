from tabnanny import check
import pyinputplus as pyip, re, sys

yesRegex = re.compile('(ye+s)|(no+)', re.IGNORECASE)

def checkIfYes(reply):
    checkYes = yesRegex.search(reply)
    if checkYes != None:
        check = re.sub('e+', 'e', checkYes.group().lower())
        check = re.sub('o+', 'o', check)
        if check == 'yes':
            return 'yes'
        else: 
            return 'no'
    else:
        return 'Please answer yes or no.'

while True:
    replyValid = pyip.inputCustom(checkIfYes, prompt="Want to know how to keep an idiot busy for hours? ")
    if  replyValid == 'yes':
        continue
    elif replyValid == 'no':
        print('Understood, have a nice day.')
        sys.exit()
    else:
        print(replyValid)
