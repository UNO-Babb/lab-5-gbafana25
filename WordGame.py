#Word Game is a knock-off version of a popular online word-guessing game.

import random

def inWord(letter, word):
    """Returns boolean if letter is anywhere in the given word"""
    return letter in word

    return False

def inSpot(letter, word, spot):
    """Returns boolean response if letter is in the given spot in the word."""
    for w in range(len(word)):
        if word[w] == letter and w == spot:
            return True

    return False

def rateGuess(myGuess, word):
    """Rates your guess and returns a word with the following features.
    - Capital letter if the letter is in the right spot
    - Lower case letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all"""
    ratingstr = ""
    for g in range(len(word)):
        if inSpot(myGuess[g], word, g):
            ratingstr += myGuess[g].upper()
        elif inWord(myGuess[g], word):
            ratingstr += myGuess[g].lower()
        else:
            ratingstr += "*"
    return ratingstr

def main():
    #Pick a random word from the list of all words
    wordFile = open("words.txt", 'r')
    content = wordFile.read()
    wordList = content.split("\n")
    todayWord = random.choice(wordList)
    #print(todayWord)

    #User should get 6 guesses to guess
    for i in range(6):
        #Ask user for their guess
        #Give feedback using on their word:
        guess = input("Make a guess: ")
        print(rateGuess(guess, todayWord))
        if guess == todayWord:
            print("You won!")
            break

    print("You lose, out of guesses")
    print("The word was "+todayWord)



if __name__ == '__main__':
  main()
