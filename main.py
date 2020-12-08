import random


def randomNumber():
    return random.randint(1, 100)


def game(count):
    gameNumber = randomNumber()
    print(gameNumber)
    print(f"You have {count} attempts.")
    userAttempt = int(input("Make a guess: "))
    while(count > 0):
        count -= 1
        print(f"You have {count} attempts remaining to guess the number.\n")
        userAttempt = int(input("Make a guess: "))

        if(userAttempt == gameNumber):
            print("YOU WIN")
            break
        if(userAttempt > gameNumber):
            print("Too high. Try again")
        if(userAttempt < gameNumber):
            print("Too low. Try again")


# user view
print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100. ")
difficulty = input("Choose a difficulty. 'easy' or 'hard': ")

if(difficulty == 'easy'):
    game(5)
elif (difficulty == 'hard'):
    game(10)
else:
    print("That option does not exist. Restart game and try again.")
    quit()
