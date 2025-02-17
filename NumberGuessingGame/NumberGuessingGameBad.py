"""
Number Guessing Game: Violating Best Practices

Violations:
1. Violates KISS - Unnecessary complexity.
2. Violates DRY - Repeats code needlessly.
3. Violates Single Responsibility - Functions do too much.
4. Violates Separation of Concerns - Logic, input, and output are mixed.
"""

import random


class NumberGuessingGameBad:
    """Poorly structured number guessing game violating best practices."""

    def __init__(self):
        self.target = random.randint(1, 100)
        self.run_game()  # Violates Single Responsibility by mixing logic in init

    def run_game(self):
        """Violates Separation of Concerns by handling everything in one function."""
        while True:
            guess = input("Enter your guess: ")
            try:
                guess = int(guess)
            except:
                print("That's not a number!")
                continue
            if guess < self.target:
                print("Too low!")
            elif guess > self.target:
                print("Too high!")
            else:
                print("You got it!")
                break
