print()

import random

def new_guess():
    guess = input('')
    guess = guess.replace(' ', '')
    guess = list(guess)
    return guess

database = []

try:
    fisier = open('cuvinte_wordle.txt')
except:
    print("Fisierul 'cuvinte_wordle.txt' nu exista")

database = [cuvant for cuvant in fisier.read().split()]

response = list(random.choice(database))

for letter in response:
    print(letter, end = ' ')
print('\n------------')

guess = new_guess()

while guess != response:
    for poz in range(5):
        if guess[poz] == response[poz]:
            print('✓', end = ' ')
        elif guess[poz] in response:
            print('✧', end = ' ')
        else:
            print('✗', end = ' ')
    else:
        print('\n')
    guess = new_guess()

print()