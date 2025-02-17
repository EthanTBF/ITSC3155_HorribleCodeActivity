import random

class NumberGuessingGame:
    """Class-based implementation of a number guessing game."""

    def __init__(self, lower=1, upper=100):
        self.lower = lower
        self.upper = upper
        self.target = random.randint(lower, upper)

    def get_user_guess(self):
        """Gets user input and ensures it is a valid integer."""
        while True:
            try:
                return int(input(f"Enter your guess ({self.lower}-{self.upper}): "))
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def check_guess(self, guess):
        """Checks the user's guess and provides feedback."""
        if guess < self.target:
            print("Too low!")
        elif guess > self.target:
            print("Too high!")
        else:
            print("Correct! You win!")
            return True
        return False

    def play(self):
        """Runs the game loop until the correct guess is made."""
        while True:
            guess = self.get_user_guess()
            if self.check_guess(guess):
                break
