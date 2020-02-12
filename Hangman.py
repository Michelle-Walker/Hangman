# Hangman game
# get random word. use random library to generate a random int
import random
import sys

file = open('words.txt', 'r')
words = []
for each_word in file:
    words.append(each_word)
n = random.randint(0, len(words))
the_word_long = words[n]
# remove the carraige return at the end of the word
short_word = the_word_long[:-1]
short_word = short_word.lower()
the_word = []
for letter in short_word:
    the_word.append(letter)

# print(' '.join(the_word)) This prints the word.
print('Starting Hangman')
display = []
for i in range(0, len(the_word)):
    display.append('_ ')
print(' '.join(display))

wrong_guess_count = -1
tot_guess = []
picture = ['O',
           'O \n|',
           ' O \n\|',
           ' O \n\|/',
           ' O \n\|/ \n/',
           ' O \n\|/ \n/ \ ']


while str(display) != str(the_word) and wrong_guess_count < 5 and tot_guess != the_word:
    user_guess = input('Guess a letter: ')

    def check(guess):
        global wrong_guess_count
        if len(guess) == 1:
            if guess.isalpha() or guess == '-' or guess == "'":
                for c in range(0, len(the_word)):
                    letter_check = the_word[c]
                    if letter_check == guess:
                        display[c] = guess
                if guess not in the_word:
                    wrong_guess_count += 1
                    print(picture[wrong_guess_count])
            else:
                print('Guess Again')
        elif len(guess) > 1:
            for each in guess:
                tot_guess.append(each)
            if tot_guess == the_word:
                print('You Win!')
                sys.exit()
            else:
                print('LOSER!')
                sys.exit()
        else:
            print('fuck off')
        if str(guess) != str(the_word) and wrong_guess_count < 5 and tot_guess != the_word:
            print(' '.join(display))
    check(user_guess)


if wrong_guess_count >= 5:
    print('Loser!')
if str(display) == str(the_word):
    print('You Win!')
