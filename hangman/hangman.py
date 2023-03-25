import random
import hangman_art
import hangman_words


word_list = hangman_words.word_list
stages = hangman_art.stages
logo = hangman_art.logo

chosen_word = random.choice(word_list)

display = ["_"] * len(chosen_word)
joined = ''
lives = 6
rightGuess = False

print("Welcome to Hangman")
print(logo)

while chosen_word != joined:

    guess = input("Enter a guess: ").lower()
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            if guess in joined:
                print("You already guessed that word.")
                print(stages[lives])
            else:
                display[i] = guess
                print(f'You have {lives} lives left, good job.. keep going.!')
                print(stages[lives])
            rightGuess = True
        
    print(display)
    
    if not rightGuess:
        lives -= 1
        if lives == 0:
            print(stages[lives])
            print(f"Game over, you suck at this. Better luck next time, the word was {chosen_word}")
            break
        else:
            print(f'You have {lives} lives left, be careful')
            print(stages[lives])

    joined = ''.join(display)

    if chosen_word == joined:
        print("you won!")

    rightGuess = False