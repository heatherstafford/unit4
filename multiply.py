#Heather Stafford
#3/30/18
#multiply.py

from random import randint


numCorrect = 0
while numCorrect < 5:
    num1 = randint(1,12)
    num2 = randint(1,12)
    answer = int(input(num1 ,'x', num2, '=' ))
    if answer == num1 * num2:
        numCorrect += 1
    else:
        print('Sorry, Incorrect')
    
        
