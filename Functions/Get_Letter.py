#getLetter


#usedLetters = [] ##enter that before using the function
def getLetter(usedLetters):
    valid = False
    while not valid:
        letter = input("Enter a single letter")
        if letter.isalpha():
            if len(letter) == 1:
                if letter in usedLetters:
                    print("That letter has already been used. Try another letter")
                else:
                    letter = letter.capitalize()
                    usedLetters.append(letter)
                    valid = True

        elif letter.isalpha():
            if len(letter) != 1:
                print("That is not correct. Please enter a single letter")

        elif not letter.isalpha():
            print("That is not correct. Please enter a single letter")


    return letter, usedLetters

letter, usedLetters = getLetter(usedLetters)

