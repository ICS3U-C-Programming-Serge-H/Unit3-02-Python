# Created by: Serge Hamouche
# Created on: march 3rd, 2025
# This program asks the user for a random number from 0-9


def main():
    # Ask user to guess number from 0-9

    # Choose a secret number (constant)
    SECRET_NUMBER = 5

    # Get the user's guess
    user_guess = int(input("Enter a number between 0 and 9: "))

    # Check if the guess is correct
    if user_guess == SECRET_NUMBER:
        print("correct!")
    else:
        print("wrong!")


if __name__ == "__main__":
    main()
