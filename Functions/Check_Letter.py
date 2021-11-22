#CheckLetter

#numBlanks = len(guessableWord)
def checkLetter(letter, guessableWord, blanks, blanksString, numBlanks):
    letterFound = False
    for i in range(len(guessableWord)):
        if letter == guessableWord[i]:
            print("Congratulations! You got the letter: " + letter)
            blanks[i] = letter
            numBlanks -= 1
            letterFound = True

    if letterFound:
        ("Sorry, that letter is not in the word")
    blanksString = ''.join(blanks)

    return blanks, blanksString

letter = input(" ")
guessableWord = 'Jeff'
blanks, blanksString = checkLetter(letter, guessableWord, blanks, blanksString)
