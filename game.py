import random

number = random.randint(1, 10)
tries = 0
uname = input("Enter your username : ")
print("Hello..! Mr.", uname, "Welcome to my game")

question = input("Do you want to play the game [Y/N]  : ")
if question == ("n"):
    print("ohh..okay")
if question == ("y"):
    print("Okay lets start the game")
    print("I am guessing a number betweeen 1 to 20 ")
    guess = int(input("you guess what the number could be : "))
    while guess != number:
        tries += 1

        if guess > number:
            guess = int(input("Guess Lower : "))
        if guess < number:
            guess = int(input("Guess Higher : "))
    if guess == number:
        print("Congrats ,you won..!")
        print("The correct number is", guess)
    print("it took you ", tries, "tries to guess the correct answer")

