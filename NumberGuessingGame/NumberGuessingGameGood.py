"""
Number Guessing Game: Good Coding Practices

Best Practices Demonstrated:
1. KISS (Keep It Simple, Stupid) - Avoids unnecessary complexity.
2. DRY (Don't Repeat Yourself) - Reduces redundancy.
3. Single Responsibility - Functions handle distinct tasks.
4. Separation of Concerns - Input handling, logic, and output are properly separated.
"""

import random


class NumberGuessingGameGood:
    """Class-based implementation of a number guessing game following best practices."""

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
