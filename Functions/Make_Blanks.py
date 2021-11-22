#makeBlanks

def makeBlanks(guessableWord):
    blanks = []
    for i in range(len(guessableWord)):
        blanks.append('*')

    blanksString = ''.join(blanks)
    return blanks, blanksString

blanks, blanksString = makeBlanks('huuhhaah')
print(blanks, blanksString)
