import random

def guessing_game():
    number = random.randint(1, 100)  # Random number between 1 and 100
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too Low! Try again.")
        elif guess > number:
            print("Too High! Try again.")
        else:
            print("Congratulations! You guessed the number.")
            print("Total attempts:", attempts)
            break

guessing_game()
