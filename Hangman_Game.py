import random

class hangman:
    def __init__(self):
        
        self.easy = random.choice([
            "car", "book", "glass", "lamp",
            "milk", "door", "star", "fish"
        ])

        self.medium = random.choice([
            "earth", "house", "turtle", "cupboard",
            "pineapple", "beach", "apple"
        ])

        self.hard = random.choice([
            "globe", "jupiter", "crocodile", "dragonfruit",
            "phillipean", "curtain", "grizzlybear"
        ])

        self.secret_words = ""
        self.lives = 6
        self.display_list = ""

    def choice(self, level):
        
        if level == 1:
            self.secret_words = self.easy

        elif level == 2:
            self.secret_words = self.medium

        elif level == 3:
            self.secret_words = self.hard

    def game_rule(self):
        self.display_list = ["_"] * len(self.secret_words)

        while self.lives > 0:

            print("\nWord:", " ".join(self.display_list))
            print("Lives:", self.lives)

            self.ask_letter = input("Guess the letter: ").lower().strip()

            if self.ask_letter in self.secret_words:
                index = 0

                for i in self.secret_words:
                    if self.ask_letter == i:
                        self.display_list[index] = self.ask_letter

                    index += 1

                print("Correct guess!")

            else:
                self.lives -= 1
                print("Wrong guess!")

            if "_" not in self.display_list:
                print("\nYou won!")
                print("The word was:", self.secret_words)
                break

        if self.lives == 0:
            print("\nYou lost!")
            print("The word was:", self.secret_words)

game = hangman()

# Real engine
print("======== HANGMAN GAME ===========")


level = int(input("""Enter the number of the level you want to play:
                    1. Easy
                    2. Medium
                    3. Hard
                    """))

game.choice(level)
game.game_rule()
