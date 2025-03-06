#Number guessing game in python

import random

def number_guessing_game():
    while True:
        random_number = random.randint(1, 100)  # Generates a random number between 1 and 100
        attempts = 0  # Counter for the number of attempts

        print("Welcome to the number guessing game!")

        while True:
            try:
                guess = int(input("Guess a number between 1 and 100: "))
                attempts += 1  # Increment the attempt counter with each guess

                if guess < random_number:
                    print("Too low! Try again.")
                elif guess > random_number:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You guessed the number in {attempts} attempts.")
                    break  # Exit the loop once the number is guessed correctly

            except ValueError:
                print("Please enter a valid number!")

        # Ask the user if they want to play again
        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay != 'yes':
            print("Thank you for playing! Goodbye!")
            break


# Run the game
number_guessing_game()
