#GetChoice

def getChoice():
    validEntry = False
    while not validEntry:
        menuChoice = input("Please make a choice: ")
        if menuChoice == '1' or menuChoice == '2':
            validEntry = True

        else:
            print("Incorrect. You must choose 1 or 2")

    return menuChoice

menuChoice = getChoice()