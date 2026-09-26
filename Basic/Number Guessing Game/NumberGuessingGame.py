import random

while True:

    # Generate random number
    number = random.randint(1, 100)

    attempts = 7
    attempts_used = 0
    guessed = False

    print("\n🎯 Number Guessing Game")
    print("Guess a number between 1 and 100")
    print("You have 7 attempts.")

    while attempts_used < attempts:

        guess = int(input("\nEnter your guess: "))

        attempts_used = attempts_used + 1

        if guess > number:
            print("Too High")

        elif guess < number:
            print("Too Low")

        else:
            print("Correct!")
            print("Attempts used:", attempts_used)
            guessed = True
            break

    if guessed == False:
        print("\nYou failed all 7 attempts!")
        print("The correct number was:", number)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break