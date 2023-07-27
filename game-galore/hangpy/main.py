import random


class Game:
    
    def __init__(self):
        self.used, self.misshits, self.password, self.password2 = [], 0, "", ""

    def check(self, guess):
        invalid_input = True

        if guess in self.used:
            print("letter already used")
        
        if guess.isalpha() and len(guess)==1 and guess not in self.used:

            if guess in self.password:
                invalid_input = False
                self.used.append(guess)
                for i in range(len(self.password)):
                    if self.password[i] == guess:
                        self.password2 = self.password2[:2*i] + guess + self.password2[2*i+1:]
                print(self.password2)
            else:
                self.misshits += 1
                print("Incorrect!")       
        else:
            print("Invalid input!")

        print(invalid_input)
        return invalid_input

    def players_turn(self):
        invalid_input = True
        while (invalid_input):
            guess = input("Enter a letter: ")
            invalid_input = self.check(guess)
            if self.misshits > 7:
                print("You lost!")
                return not invalid_input, self.password2
        print(not invalid_input)
        return not invalid_input, self.password2
            
    def start(self):
        self.used = []
        self.misshits = 0
        guessed = 0
        
        word_list = open("words2.txt").read().splitlines()
        self.password = random.choices(word_list)[0]
        self.password2 = len(self.password) * "_ "
        print("Welcome to hangman game!")
        while guessed < len(self.password):
            correct = self.players_turn()
            if correct:
                guessed += 1
            if self.misshits > 7:
                return
        print(f"You won with {self.misshits}/7 misshits! Congrats!")

if __name__ == "__main__":
    game = Game()
    play_again = "yes"
    while play_again == "yes":
        game.start()
        print("Game over!")
        play_again = input("Do you want to play again? (yes/no): ")
'''
  -----------
  | /   |
  |/    O
  |    /|\
  |     ^
  |    / \
  |
-----------------'''