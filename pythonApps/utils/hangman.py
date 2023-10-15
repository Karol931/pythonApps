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

    guessed_word = ('_' * len(original_word)).strip()
    
    return original_word, guessed_word, life_count

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