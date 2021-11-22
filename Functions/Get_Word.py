#GetWord

def getWord():
    print("Player one please come on the computer")
    wordValid = False

    while not wordValid:
        guessableWord = input("Please enter a word for your opponent to guess")
        guessableWord = guessableWord.capitalize()

        if guessableWord.isalpha():
            wordValid = True

        if not guessableWord.isalpha():
            print("Thats not a valid word, please only enter letters [Case insensitive]")

    return guessableWord

getWord()