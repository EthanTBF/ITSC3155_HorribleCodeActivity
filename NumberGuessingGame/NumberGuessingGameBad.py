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
    """Terribly structured guessing game that makes life difficult."""

    def __init__(self):
        self.magic_number_of_eternal_suffering = random.randint(1, 10000)
        self.guess_the_number_or_perish()

    def guess_the_number_or_perish(self):
        """Mashes everything together in a confusing mess."""
        while True:
            user_proclamation_of_doom = input("Take a wild guess at the number, you have to lock in for this one: ")
            try:
                user_proclamation_of_doom = int(user_proclamation_of_doom)
            except:
                print("Bro that isn't even a number, are you even trying? ( ͡° ͜ʖ ͡° ) ")
                continue
            if user_proclamation_of_doom < self.magic_number_of_eternal_suffering:
                print("THAT'S TO LOW, GUESS AGAIN! ᕙ(⇀‸↼‶)ᕗ ")
            elif user_proclamation_of_doom > self.magic_number_of_eternal_suffering:
                print("Too high! You better start guessing LOWER! Ⴚტ⊙▂⊙ტჂ ")
            else:
                print("You have somehow stumbled upon the correct number. Unbelievable, are you hacking? (ノಠ益ಠ)ノ彡┻━┻ ")
                break
