import pyinputplus as pyip, random, time

numberOfQuestions = 10
correctAnswers = 0

for questionsNumber in range(numberOfQuestions):
    num1 = random.randint(2,20)
    num2 = random.randint(2,20)

    prompt = '#%s: %s x %s = ' % (questionsNumber, num1, num2)

    try:
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1*num2)],
                              blockRegexes=[('.*', 'Incorrect!')],
                              timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print('Correct!')
        correctAnswers += 1
    
    time.sleep(1)

print('Score: %s / %s' % (correctAnswers, numberOfQuestions))