# a game where you have to find what is 
# the number that the machine guessed
# with as few tries as possible

import random
x = random.randint(1,1001)
guess = input("Okay, I have a number between 1 and 1000. Guess what that number is : ")
number = False
n=1
while number == False:
    try:
        guess = int(guess)
        number = True
    except ValueError:
        print("\n Please enter a number only")
        guess = input("guess a number between 1 and 1000: ")
    
        

while guess != x:
    if guess > x:
        print("\n nah, lower")
        print("You tried %s times" %n)
        guess = int(input("guess again: "))
    elif guess < x:
        print("\n nah, higher")
        print("You tried %s times" %n)
        guess = int(input("guess again: "))
    n+=1

    
print("Yeah correct. My number was %s" %x)
print("You tried %s times" %n)
