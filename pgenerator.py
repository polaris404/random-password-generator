import random
import re

with open("eff_large_wordlist.txt", "r") as f:
    WORDS = f.readlines()


def get_index():
    index = ""
    for i in range(5):
        index += str(random.randint(1, 6))
    return index


def get_words(number=4):
    words_used = []
    for i in range(number):
        index = get_index()
        for line in WORDS:
            if line.strip().startswith(index):
                word = re.search(r"[a-z-]+", line).group()
                words_used.append(word)
                break
    return words_used


def add_cap_letters(string):
    for i in range(random.choice([2, 3])):
        index = random.randrange(0, len(string))
        string = string[:index] + string[index].upper() + string[index + 1 :]
    return string


def add_digits(string):
    DIGITS = range(0, 9)
    for i in range(random.choice([2, 3])):
        index = random.randrange(len(string))
        string = string[:index] + str(random.choice(DIGITS)) + string[index:]
    return string


def add_symbols(string):
    SYMBOLS = ["!", "@", "#", "&", "-", "_", ".", "^"]
    for i in range(random.choice([2, 3])):
        index = random.randrange(len(string))
        string = string[:index] + random.choice(SYMBOLS) + string[index:]
    return string


def add_complexity(string):
    string = add_symbols(add_cap_letters(string))
    return string
