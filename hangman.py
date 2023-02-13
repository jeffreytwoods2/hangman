from random import randint
from time import sleep

WORD_LIST = ["hello", "goodbye", "whaddup"]

GRAPHICS_LIST = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def getWord():
    with open("wordlist.txt") as word_file:
        word_list = word_file.readlines()
        total_words = len(word_list)
        random_index = randint(0, total_words)
        chosen_word = word_list[random_index].replace("\n", "")
    
    return chosen_word, total_words

def main():
    play_again = True
    total_tries = len(GRAPHICS_LIST) - 1


    while play_again == True:
        hangman_state = 0
        word, word_count = getWord()
        current_state = []
        used_letters = []

        for i in range(0, len(word)):
            current_state.append("_")

        print(f"This word has {len(word)} letters.")
        print(GRAPHICS_LIST[0])

        for i in range(0, len(current_state)):
                print(current_state[i] + " ", end="")

        while hangman_state < total_tries:
            print("""


Used Letters:""", end=" ")
            for i,l in enumerate(used_letters):
                print(l + " ", end="")
            
            guess = input("\n\nGuess a letter:\n> ")
            
            if len(guess) != 1:
                print("Type a single letter.")
                continue
            elif guess in used_letters:
                print("You already tried that.")
                continue
            elif guess in word:
                for letter_place in (idx for idx, l in enumerate(word) if l==guess):
                    current_state[letter_place] = guess
                print("Nice!")
                used_letters.append(guess)
            else:
                print("Nope")
                used_letters.append(guess)
                hangman_state += 1
            
            if "_" not in current_state:
                for i in range(0, len(current_state)):
                    print(current_state[i] + " ", end="")
                print("\nYou win!")
                break

            print(GRAPHICS_LIST[hangman_state])

            for i in range(0, len(current_state)):
                print(current_state[i] + " ", end="")

        if hangman_state == total_tries:
            print("\nGame over.")
            print(f"The word was {word}.")

        while True:
            keep_playing = input("Would you like to play again? y/n\n> ")

            if keep_playing == "n":
                play_again = False
                break
            elif keep_playing != "y":
                print("Please type \'y\' or \'n\'")
            else:
                break

if __name__ == "__main__":
    main()