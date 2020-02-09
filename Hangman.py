# Hangman game
import random
# get random word
print('Starting Hangman')
# guess = input('Guess a letter: ')
n = random.randint(0, 100)
file = open('words.txt', 'r')
print(file.readline(1))
print(n)