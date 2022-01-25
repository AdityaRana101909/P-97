import random
print('NUMBER GUESSING GAME')
chances=5
print('Choose a number between 1 and 9')
number= random.randint(1,9)
guess=input('Take a Guess')
print(guess)
while chances>0:
     if guess==number:
        print('Correct Answer. You Won!!')
        

     if guess!=number:
         print('Incorrect Answer. Try again')
chances=chances-1