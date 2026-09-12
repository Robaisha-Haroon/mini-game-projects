# game of guessing number

import random
a= random.randint(1,50)

while True:
    user_guess= int(input("guess a number"))
    if user_guess == a:
        print('you are right\n')
        break
    elif user_guess < a:
        print("choose higher number")
    else:
        print("choose lower number")
print("you won 🎉")
