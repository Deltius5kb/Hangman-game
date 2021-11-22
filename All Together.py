hasattr#all together
import random

#DisplayMenu

def printMenu():
    displayMenu = '''
    Choose an option for what mode you want to play
    [1] Easy mode - Play a game with a friend
    [2] Difficult mode - Play a game with the computer

    '''
    print(displayMenu)

#GetChoice

def getChoice():
    validEntry = False
    while not validEntry:
        menuChoice = int(input("Please make a choice: "))
        if menuChoice == 1 or menuChoice == 2:
            validEntry = True

        else:
            print("Incorrect. You must choose 1 or 2")

    return menuChoice

#GetWord

def getWord():
    print("Player one please come on the computer")
    wordValid = False

    while not wordValid:
        guessableWord = input("Please enter a word for your opponent to guess")
        guessableWord = guessableWord.upper()

        if guessableWord.isalpha():
            wordValid = True

        if not guessableWord.isalpha():
            print("Thats not a valid word, please only enter letters [Case insensitive]")

    return guessableWord

#chooseWord

def chooseWord():
    words = ['PIZZAZ', 'JACUZZI', 'JUKEBOX', 'DRIZZLY', 'ZIGZAGS']
    word = words[(random.randint(0, 4))]
    ####words = open("guessableWords.txt").readlines()
    ###word = words[0]
    ####while not word.isalpha():
    ###    word = random.choice(words)

    ###wordList = list(word)
    ###wordList.pop()
    return word

#makeBlanks

def makeBlanks(guessableWord):
    blanks = '*' * len(guessableWord)
    return blanks

#getLetter

#usedLetters = [] ##enter that before using the function
def getLetter(usedLetters, blanks, numWrong):
    valid = False
    while not valid:
        print("Letters used:", usedLetters)
        print("Attempts remaining:", numWrong)
        print(blanks)
        letter = input("Enter a single letter")
        if letter.isalpha():
            letter = letter.capitalize()
            if len(letter) == 1 and letter not in usedLetters:
                letter = letter.capitalize()
                usedLetters.append(letter)
                valid = True
            else: print("You have already used this letter")

        elif letter.isalpha():
            if len(letter) != 1:
                print("That is not correct. Please enter a single letter")

        elif not letter.isalpha():
            print("That is not correct. Please enter a single letter")

    return letter, usedLetters, numWrong

#CheckLetter

#numWrong = 7
def checkLetter(letter, guessableWord, blanks, numWrong, numBlanks):
    letterFound = False
    blanks = list(blanks)
    for i in range(len(guessableWord)):
        if guessableWord[i] == letter:
            if letterFound == True:
                print("Congratulations! You got the letter: " + letter)
            numBlanks -= 1
            blanks[i] = letter
            letterFound = True

    if not letterFound:
            ("Sorry, that letter is not in the word")
            numWrong -= 1
    blanks = ''.join(blanks)
    return blanks, numWrong, numBlanks

#int main()

retry = True
while retry:
    printMenu()

    choice = getChoice()

    if choice == 1:
        guessableWord = getWord()

    if choice == 2:
        guessableWord = chooseWord()

    blanks = makeBlanks(guessableWord)

    numBlanks = len(guessableWord)
    numWrong = 7
    usedLetters = []
    while numWrong > 0 and numBlanks > 0:
        letter, usedLetters, numWrong = getLetter(usedLetters, blanks, numWrong)
        blanks, numWrong, numBlanks = checkLetter(letter, guessableWord, blanks, numWrong, numBlanks)

    if numWrong == 0:
        print("Sorry you lost, the man was hanged")

    if numBlanks == 0:
        print("The guesser has guessed the word")

    print("Letters used: " + (''.join(usedLetters)))
    guessableWord = guessableWord.capitalize()
    print("The word was: " + guessableWord)
    print('''
    Would you like to play again?
    1] Yes
    2] No
    ''')
    playAgain = getChoice()
    if playAgain == 1:
        retry = True

    else:
        retry = False


