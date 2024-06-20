import random

from hangman_art import stages,logo
from hangmanwords import word_list
chosen_word=random.choice(word_list)
chosen_word_list=[]
end_of_game=False
lives=6
print(logo)
#creating blanks
guess_word=[]
for i in range(0,len(chosen_word)):
    guess_word.append("_")
print(guess_word)

while not end_of_game:
        guess=input("guess a letter").lower()
        if guess in guess_word:
            print("already guessed the letter guess again")
        #checking if the letter is present
        for position in range(0,len(chosen_word)):
            letter=chosen_word[position]
            if guess==letter:
                guess_word[position]=guess
        print(guess_word)
        #if not present
        if guess not in chosen_word:
            print(f"the letter {guess} is not in word")
            lives -= 1
            print(stages[lives])
            if lives==0:
                print("you lost")
                end_of_game=True

      #checking if all letters are filled
        if "_" not in guess_word:
            print("you won")
            end_of_game=True
