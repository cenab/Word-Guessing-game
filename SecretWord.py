from Node import Node

class LinkedList:
    """ The Singly-Linked List class defined in lecture """

    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.head == None

    def length(self):
        return self.size

    def add(self, item):
        temp = Node(item, None)
        temp.setNext(self.head)
        self.head = temp
        self.size += 1

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def index(self, item):
        current = self.head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                index = index + 1
        if not found:
            index = -1
        return index
    
    def getNode(self, item):
        #iterate through all the nodes and when it finds the spesific node and returns to that node and a previous node
        previous = None
        current = self.head 
        while current != None and current.getData() != item: 
            previous = current
            current = current.getNext()
        return current, previous
    
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

        self.size -= 1

        return found

    def append(self, item):
        temp = Node(item, None)
        if self.head == None:
            self.head = temp
        else:
            current = self.head
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(temp)
        self.size += 1

    def pop(self):
        current = self.head
        previous = None
        while current.getNext() != None:
            previous = current
            current = current.getNext()

        if previous == None:
            self.head = None
        else:
            previous.setNext(None)
        self.size -= 1
        return current.getData()

    def getHead(self):
        return self.head
    
    def searchIndex(self, index):
        #iterates through the linked list and when it comes to a spesific index it returns to that node
        current = self.head
        while index != 0:
            current = current.getNext()
            index -= 1
        return current
    
    def update(self, item):
        #iterates through the list and if it coincides with a given item it just turns its display to true, this function is written for update function below
        current = self.head
        a = 0
        while current != None:
            if current.getData() == item:
                current.setDisplay(True)
                a += 1
            current = current.getNext()
        if a != 0:
            return True
        else:
            return False        

class SecretWord:

    def __init__(self):
        self.linkedList = LinkedList()

        # Additional attribute(s) go here:

    def setWord(self, word):
        #appends every letter of the word to the link list
        """ Adds the characters in 'word' to self.linkedList in the given order """
        for letter in word:
            self.linkedList.append(letter)
        return

    def sort(self):
        #adaptation of insertion sort to the link lists, it starts from first index and checks if elements before that index are bigger than or smaller than that value by using
        #ord function and if it finds smaller value, it justs shifts the item by changing nodes' datas
        """ Sorts the characters stored in self.linkedList in alphabetical order """
        for index in range(1, self.linkedList.length()):
            temp = self.linkedList.searchIndex(index).getData()
            position = index
            while position > 0 and ord(self.linkedList.searchIndex(position-1).getData()) > ord(temp):
                self.linkedList.searchIndex(position).setData(self.linkedList.searchIndex(position-1).getData())
                position = position -1
            self.linkedList.searchIndex(position).setData(temp)
        
    def isSolved(self):
        """ Returns whether SecretWord has been solved (all letters in the word have been guessed by the user) """
        #iterates through every node in the list and if one display is True, the function returns to False
        current = self.linkedList.getHead()
        index = self.linkedList.length()
        while index != 0:
            if current.getDisplay() == True:
                return False
            current = current.getNext()
            index -= 1
        return True

    def update(self, guess):
        #please check the update function above
        """ Updates the nodes in self.linkedList that match 'guess' """
        if self.linkedList.update(guess) == True:
            return True
        else:
            return False

    def printProgress(self):
        """ Prints the current game progress
        Ex: y _ l l _ w """
        #iterates through every node and if a display is True, it prints the data of the node. Otherwise it prints "_"
        current = self.linkedList.getHead()
        index = self.linkedList.length()
        while index != 0:
            if current.getDisplay() == True:
                print(current.getData(), end = ' ')
            else:
                print('_', end = ' ')
            current = current.getNext()
            index -=1
    
    def getProgress(self):
        #iterates through every node and checks if their dispay is True, if it is True it adds the letter to the string. Otherwise it adds "_" and returns the string
        current = self.linkedList.getHead()
        index = self.linkedList.length()
        progresslist = []
        while index != 0:
            if current.getDisplay() == True:
                progresslist.append(current.getData())
            else:
                progresslist.append('_')
            current = current.getNext()
            index -=1
        return ' '.join(progresslist)
    
    def getProgressNoSpace(self):
        #iterates through every node and checks if their dispay is True, if it is True it adds the letter to the string. Otherwise it adds "_" and returns the string
        #same function as above except there is no space inbetween the letters
        current = self.linkedList.getHead()
        index = self.linkedList.length()
        progresslist = []
        while index != 0:
            if current.getDisplay() == True:
                progresslist.append(current.getData())
            else:
                progresslist.append('_')
            current = current.getNext()
            index -=1
        return ''.join(progresslist)    
        
    def __str__(self):
        #iterates through the nodes and turns it to a string
        """ Converts the characters in self.linkedList into a string """
        current = self.linkedList.getHead()
        index = self.linkedList.length()
        string = ''
        while index != 0:
            string = string + current.getData() 
            current = current.getNext()
            index -=1
        return string
    
    def getWord(self):
        #turns it into string
        current = self.linkedList.getHead()
        index = self.linkedList.length()
        string = ''
        while index != 0:
            string = string + current.getData() 
            current = current.getNext()
            index -=1
        return string        
