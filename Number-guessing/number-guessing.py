import art
import random

print(art.logo)

print("welcome to the number guessing game.!")
print("I'm thinking of a number between 1 and 100")
guess_comp = random.randint(1,100)
difficulty = input("Choose a difficulty. Type 'easy or 'hard': ").lower()
chances = 5
won = False
if difficulty == 'easy':
  chances = 10

def check_guess(guess):
  if guess > guess_comp:
    print("Too High!")
    print("Guess again.")
    print(f"You have {chances} guesses remaining.")
    return
  elif guess < guess_comp:
    print("Too low!")
    print("Guess again.")
    print(f"You have {chances} guesses remaining.")
    return
  else:
    print("You won!")
    global won
    won = True
    return

print(f"You have {chances} attempts to guess the number.")
while chances > 0:
  guess_player = int(input("Make a guess: "))
  chances -= 1
  check_guess(guess_player)
  if won:
    break
  elif chances == 0:
    print("Sorry, you suck at this..")
    break