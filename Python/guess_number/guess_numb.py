import random

name = input("What is your name? ")
start = input(f"Hello, {name}. Would you like to play a game? ")
if start.lower() == "yes":
    print("Fun! Let's play")
else:
    print("Awh, oki bye")
    quit()

#initialize
def guess(x):
    random_numb = random.randint(1,x)
    guess = 0
    turn_counter = 0
    

#step 2: guess the number; loop until right answer
    while turn_counter <5:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        #turn counter
        turn_counter+=1
        #tells us if number is too high, low, or correct
        if guess < random_numb:
            print('Youre guess is too low')
        elif guess > random_numb:
            print("Your guess is too high")
        else:
             guess == random_numb
             break

            
    if guess==random_numb:
        print("Wao, you guessed it right in " +str(turn_counter)+ " guesses!")
    else:
        print("Sorry, the number I am thinking is " +str(random_numb))
        print("Let's play again next time!")

guess(50)

