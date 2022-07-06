import random

def guess(x):
    randomNum = random.randint(1,x);
    guess = 0
    count = 0

    while guess != randomNum:
        guess = int(input("Guess a number between 1 and %d: " % x))
        count+=1
        if guess < randomNum:
            print("The magic number is HIGHER than your previous guess. Try again.")
        elif guess > randomNum:
            print("The magic number is LOWER than your previous guess. Try again.")

    print("Congrats! You guessed the magic number %d in %d iteration(s). " % (x, count))        

x = input("Welcome to the game! Pick a number and you will have to guess a magic number \
between 1 and your picked number: ")

guess(int(x))