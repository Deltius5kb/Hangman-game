#chooseWord
import random

def chooseWord():
    words = ['PIZZAZ', 'JACUZZI', 'JUKEBOX', 'DRIZZLY', 'ZIGZAGS']
    word = words[(random.randint(0, 4))]
    #words = open("guessableWords.txt").readlines()
    #word = words[0]
    #while not word.isalpha():
    #    word = random.choice(words)

    #wordList = list(word)
    #wordList.pop()
    return word

guessableWord = chooseWord()
print(guessableWord)