import random
import os

logo = '''
 ___                        _    _                           _              _ 
/  _>  _ _  ___  ___ ___  _| |_ | |_  ___  ._ _  _ _ ._ _ _ | |_  ___  _ _ | |
| <_/\| | |/ ._><_-<<_-<   | |  | . |/ ._> | ' || | || ' ' || . \/ ._>| '_>|_/
`____/`___|\___./__//__/   |_|  |_|_|\___. |_|_|`___||_|_|_||___/\___.|_|  <_>
     
'''

def play():
    print(logo)
    print("Welcome to the number guessing game!")
    print("Computer thinking of a number between 1 and 100...")
    difficulty = input("Choose the difficulty. Type 'easy', 'medium', 'hard' or 'impossible': ").lower()
    computer_guess = random.randint(1,100)

    def difficulties():
        if difficulty == "easy":
            attempts = 15
        elif difficulty == "medium":
            attempts = 10
        elif difficulty == "hard":
            attempts = 5
        else:
            attempts = 1
        return attempts
    attempts = difficulties()

    guess = ""      
    while attempts > 0 and guess != computer_guess:
        print(f"You have {attempts} attempts to guess the number.")
        guess = int(input("Make a guess: "))
        if guess < computer_guess:
            attempts -= 1
            print("Try higher!")
        elif guess > computer_guess:
            attempts -= 1
            print("Try lower!")
        elif guess == computer_guess:
            os.system("cls")
            print(logo)
            print(f"Congratulations! You guessed the number! The computer's guess was {computer_guess}.")
        if attempts == 0:
            os.system("cls")
            print(logo)
            print(f"It's a shame, but you lose! The computer's guess was {computer_guess}.")
play()
while input("Want to play again? y/n -> ").lower() == "y":
    os.system("cls")
    play()