import random

number = random.randrange(21)
guess = input("Guess the the number! It's number between 0 and 20! \n")
check = True
while check:
    if guess.isdigit():
        guess = int(guess)
        if guess == number:
            print("Correct! You guessed it!")
            check = False
        elif guess > number:
            guess =input("It's too big! Try again! \n")
        else:
            guess = input("It's too small! Try again! \n")
    else:
        guess = input("It's not a number! Try again! \n")