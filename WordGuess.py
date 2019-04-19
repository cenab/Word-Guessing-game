import random
from SecretWord import SecretWord

class WordGuess:
    def __init__(self, wordDic):
        self.__worddict = wordDic
        self.__secretword = None
        self.__anotherword = None
        self.__hint = None
        self.__guesses = 10
        self.__b = SecretWord()
        self.__a = SecretWord() 
        return
    
    def beforePlay(self):
        #setting up everything before the game
        self.chooseSecretWord()
        self.editDistance(self.__a.getWord(), self.__b.getWord())
        self.amountGuess()
        return len(self.__b.getProgress())

    def play(self):
        #plays the game once, print the process of the game and gets an input and if the letter is correct it updates it or if it is false and deletes one from guesses and prints the guesses
        """ Plays out a single full game of Word Guess """
        if self.getProgressNoSpace().isalpha() == False:
            print('Word Guess Progress: %s'%(self.__b.getProgress()))
            n = self.getGuess()
            if self.__b.update(n) == False:
                self.__guesses -= 1
                print('You have %d guesses remaining'%(self.__guesses))
        else:
            print('You solved the puzzle!')        
        return self.__secretword
    
    def isSolved(self):
        return self.__b.isSolved()
    
    def getProcess(self):
        return self.__b.getProgress()
    
    def getProgressNoSpace(self):
        return self.__b.getProgressNoSpace()
    
    def chooseSecretWord(self):
        #gets the dictionary from the main file and gets a random number. Chooses a name from the list using the random created number as an index and using that randomly choosen word, we are
        #getting the hint from the dictionary
        """ Chooses the secret word that will be guessed """
        listword = []
        randomintiger = random.randint(0, len(self.__worddict)-1)
        for key in self.__worddict:
            listword.append(key)
        self.__secretword = listword[randomintiger]
        self.__hint = self.__worddict[self.__secretword]
        self.__b.setWord(self.__secretword)
        self.__a.setWord(self.__secretword)
        self.__a.sort()
        return self.__secretword

    def editDistance(self, s1, s2):
        #a part of this fucntion is adapted from this webside and the way it recurse the word is different: https://www.geeksforgeeks.org/edit-distance-dp-5/
        """ Recursively returns the total number of insertions and deletions required to convert S1 into S2 """
        if len(s1) == 0:
            return len(s2) #our base case which helps us stop the function, this basically returns to zero most of the time so just the amount of moves are left        
        if len(s2) == 0:
            return len(s1)
        if s1[0] == s2[0]:
            moves = 0 #if the first letters are the same, there is no move to be made
            return self.editDistance(s1[1:], s2[1:])#it returns to editdistance except the first letter of the string
        else:
            moves = 1 #since it is not the same there is an action to be made
        return min([self.editDistance(s1[1:], s2), self.editDistance(s1, s2[1:]), self.editDistance(s1[1:], s2[1:])]) + moves #if the next letter of one of these functions are same with the current letter
    #in this case we delete just one letter instead of two
    
    def amountGuess(self):
        #sets up the amount of guesses player have 
        if self.__guesses == None:
            self.__guesses = 2 * self.editDistance(self.__b.getWord(), self.__hint)
        return self.__guesses
    
    def getNumberGuess(self):
        return self.__guesses

    def getGuess(self):
        #until player answer the question like it is intended to it continues to ask the user to take an action. There is error handling since we are getting an input, player may try to input intiger
        #we wanna avoid that
        """ Queries the user to guess a character in the secret word """
        try:
            n = input(str('Enter a character that has not been guessed or * for a hint: '))
        except:
            self.amountGuess()
        if n.isalpha() == False and n != '*':
            self.getGuess()
        if n.isalpha() == True:
            n = n.lower()
        if n == '*':
            print('Hint: %s'%(self.__hint))
        return n
