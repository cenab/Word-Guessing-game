from WordGuess import WordGuess

def readWords(filename):
    """ Read in the list of possible secret words and their corresponding hints """
    #opens up a text file and grabs all of the text and puts into dictionary to be able to use them 
    file = open(filename, 'r')
    fileread = file.read()
    wordlist = fileread.split('\n')
    wordlist2 = []
    worddict = dict()
    for i in range(len(wordlist)):
        wordlist2.append(wordlist[i].split(' '))    
        worddict[wordlist2[i][0]] = wordlist2[i][1]
    return worddict

def main():
    #runs every function that is needed for game to function properly
    filename = input(str('Please enter a Word Guess input file:'))
    worddict = readWords(filename)
    b = WordGuess(worddict)
    b.beforePlay() #guess and other variables are created here
    while b.getNumberGuess() != 0  and b.getProgressNoSpace().isalpha() == False: #until the game comes to a conclusion by reaching two outcomes, it continues to ask to continue the game
        n = b.play()
    if b.getNumberGuess() == 0:
        print('You are out of your guesses!')
        print('The secret word was: %s'%(n))
        gameover = ''
        while gameover.lower() != 'y' or gameover.lower() != 'n':
                gameover = input(str('Would you like to play again? (y/n): '))
                if gameover.lower() == 'y':
                    main()
                elif gameover.lower() == 'n':
                    print('Goodbye!')
                    break
    elif b.getProgressNoSpace().isalpha() == True:
        print('You solved the puzzle!')
        print('The secret word was: %s'%(b.getProcess()))
        gameover = ''
        while gameover.lower() != 'y' or gameover.lower() != 'n':
                    gameover = input(str('Would you like to play again? (y/n): '))
                    if gameover.lower() == 'y':
                        main()
                    elif gameover.lower() == 'n':
                        print('Goodbye!')
                        break
            
    return
if __name__ == "__main__":
    main()
