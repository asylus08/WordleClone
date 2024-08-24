import random

def initialize_word_bank():
    with open("word_bank.txt", 'r') as file:
        return [line.strip() for line in file]

def choose_word():
    dictionnary = initialize_word_bank()
    return dictionnary[random.randint(0, len(dictionnary) - 1)]