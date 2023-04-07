
import art
import random
from game_data import data

print(art.logo)
score = 0
hasLost = False

def getRand():
  return random.choice(data)

def nonUniqs(first, second):
  while second == first:
    second = getRand()
  
firstCard = getRand()
secondCard = getRand()
nonUniqs(firstCard, secondCard)

def game():
  print(f"Compare A: {firstCard['name']}, {firstCard['description']}, from {firstCard['country']}")
  print(art.vs)
  print(f"Against B: {secondCard['name']}, {secondCard['description']}, from {secondCard['country']}")
  
game()

while not hasLost:
  choice = input("Who has more followers? Type 'A' or 'B': ")
  if choice == 'A' and firstCard['follower_count'] > secondCard['follower_count']:
    score += 1
    print(f"You're right, current score: {score}")
    firstCard = secondCard
    secondCard = getRand()
    nonUniqs(firstCard, secondCard)
    game()
  elif choice == 'B' and firstCard['follower_count'] < secondCard['follower_count']:
    score += 1
    print(f"You're right, current score: {score}")
    firstCard = secondCard
    secondCard = getRand()
    nonUniqs(firstCard, secondCard)
    game()
  else:
    hasLost = True
    print(f"Sorry, that's wrong, final score: {score}")