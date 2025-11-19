import random
logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""

# TODO 1: print the welcome message and the range the computer is thinking.
print("Welcome to Guessing Game:")
print(logo)
# TODO 2: ask if the player want to play hard level or easy level
choice_level = input("Do you want to play the Hard level or Easy level? 'H' or 'E': ").lower()

# TODO 3 : Set number of allowed guesses
if choice_level == "h":
    wrong_guess = 5
else:
    wrong_guess = 10

# TODO 4: Generate random number between 1 -100 and set to correct number variable
correct_number = random.randint(1, 100)
print("I am thinking of a number between 1 and 100...")


# TODO 5: create compare function so to reduce code repeating  and make the code clean
def compare_number(guess, win_number):
    if guess > win_number:
        print("Too high!")
    elif guess < win_number:
        print("Too low!")
    else:
        print(f"🎉 Correct! The number was {win_number}. You win!")


while wrong_guess > 0:
    print(f"You have {wrong_guess} guesses left.")
    guess_number = int(input("Enter your guess: "))
    compare_number(guess_number, correct_number)
    wrong_guess -= 1
if wrong_guess == 0:
    print(f"😢 You've run out of guesses. The number was {correct_number}.")





