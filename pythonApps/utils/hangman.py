import requests
from dotenv import load_dotenv
import os

# Uses api to get random word
def get_word():
    load_dotenv()

    api_key = os.getenv('X_API_KEY')
    url = 'https://api.api-ninjas.com/v1/randomword' 
    headers = {'X-Api-Key': api_key}
    
    response = requests.get(url=url, headers=headers)
    if response.status_code == requests.codes.ok:
        word = response.json()
        return word['word']
    else:
        exit('Can\'t get random word')

# Gets begining parameters to the game
def start():
    life_count = 3

    original_word = get_word().lower()
    print(original_word)

    guessed_word = ('_' * len(original_word)).strip()
    
    print("Your word is, guess a letter:\n")

    return original_word, guessed_word, life_count

# Checks if input is valid
def input_check(letter, original_word, guessed_word, lifes):

    if len(letter) != 1:
        print("Type only one letter")
        game(original_word, guessed_word, lifes)
    if not letter.isalpha():
        print("It's not a letter")
        game(original_word, guessed_word, lifes)

# Checks if letter is in the word
def letter_check(letter, original_word):

    indexes = [i for i, ch in enumerate(original_word) if letter == ch]
    return indexes


# Inserts guessed letters into the word
def update_word(indexes, letter, guessed_word):
    s = list(guessed_word)

    for i in indexes:
        s[i] = letter
    
    guessed_word = "".join(s)

    return guessed_word


def game(original_word, guessed_word, lifes, letter):
    if lifes == 0:
        exit(f"Game Over, word was {original_word}")
    
    print()
    print('\u2764\uFE0F \t' * lifes)
    print(guessed_word)
    
    if '_' not in guessed_word:
        exit("Congratulations you won!!")
    
    input_check(letter, original_word, guessed_word, lifes)
    
    indexes = letter_check(letter, original_word)
    
    if not indexes:
        lifes -= 1
        if lifes != 0:
            print("Wrong, guess again")
        game(original_word, guessed_word, lifes)
    
    guessed_word = update_word(indexes, letter, guessed_word)

    return original_word, guessed_word, lifes