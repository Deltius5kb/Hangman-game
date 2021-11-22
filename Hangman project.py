'''
Hangman Project V0.00.01
'''
import random

def choice():
    displayMenu = '''
    Choose an option for what mode you want to play
    [1] Easy mode - Play a game with a friend
    [2] Easyn't mode - Play a game with the computer

    Please enter the number below:
    '''
    menuChoice = input(displayMenu)

    if menuChoice == '1' or menuChoice == '2':
        return menuChoice
    else:
        print("Incorrect. You must choose 1 or 2")
        choice()

def PVP():
    print("Player one please come on the computer")
    wordValid = False

    while not wordValid:
        guessableWord = input("Please enter a word for your opponent to guess")
        guessableWord = guessableWord.capitalize()

        for i in range(len(wordValid)):
            x = ord(wordValid[i])
            if x>=91 and x<=65:
                wordValid = True

        if not wordValid:
            print("Thats not a valid word, please only enter letters [Case sensitive]")
    return guessableWord

def PVE():
    difficultyChoice = 0
    while difficultyChoice < 1 or difficultyChoice > 3:
        difficultyChoice = int(input('''
        Please choose a difficulty:
            1- Easy
            2- Medium
            3- Hard
            4- Godly
        '''))

    if difficultyChoice == 1:
        words = ['COW', 'CAT', 'DOG', 'MOW', 'CLEAN', 'DREAM']
    elif difficultyChoice == 2:
        words = ['CROWBAR', 'MAXIMUM', 'MINIMUM', 'COMPUTER', 'DIFFUSION']
    elif difficultyChoice == 3:
        words = ['MICROORGANISMS', 'ALUMINIUM', 'OSMIUM', 'CONFUSION']
    elif difficultyChoice == 4:
        words = ['']

    guessableWord = words[random.randint(0, len(words))]
    return guessableWord

def guessingPhase(guessableWord):
    currentGuess = input("Enter a word or letter")

    if currentGuess == guessableWord:
        print("Congratulations! Player 2 has won the game")

    if len(currentGuess) == 1:
        for i in range(len(currentGuess)):
            if currentGuess == guessableWord[i]:



playerChoice = choice()
if playerChoice == 1:
    guessableWord = PVP()

elif playerChoice == 2:
    guessableWord = PVE()

