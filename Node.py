class Node:
    def __init__(self, initData, initNext):
        """ Constructs a new node and initializes it to contain
        the given object (initData) and link to the given next node. """

        self.data = initData
        self.next = initNext
        self.__guess =  False

        # Additional attributes

    def getData(self):
        """ Returns the element """
        return self.data

    def getNext(self):
        """ Returns the next node """
        return self.next

    def getDisplay(self):
        #gets the display of the character
        return self.__guess
    

    def setData(self, newData):
        """ Sets newData as the element """
        self.data = newData

    def setNext(self, newNext):
        """ Sets newNext as the next node """
        self.next = newNext

    def setDisplay(self, newDisplay):
        #decides if a character is going to be displayed
        self.__guess = newDisplay
        return self.__guess
