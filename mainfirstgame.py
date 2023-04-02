import random
 


random=random.choice(range(1,100))
count=1
guess=input("please enter a number from 1 to 100")
guess=int(guess)

while (True):


    if guess==random :
         print("You Won")
         print("You have tried",count,"times to win \n"
                "Final Score =", 100-count)
         break
    if guess > random :
        print("You Are Close")
        guess=input("enter a smaller one")
        count += 1
        guess=int(guess)
        if guess > random :
            guess = input("enter a SMALLER one!!!, are you idiot???")
            count += 1
            guess = int(guess)
    if guess < random:
        print("You Are Close")
        guess = input("enter a bigger one")
        count += 1
        guess = int(guess)
        if guess < random :
            guess = input("enter a BIGGER one!!!, are you out of your mind???")
            count += 1
            guess = int(guess)



