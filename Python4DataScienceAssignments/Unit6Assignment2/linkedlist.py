# This is a comment
#
#  Simple implementation of a singly linked list
#

class Node(object):
    
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode

class linkedList(object):
    nodestack=[]
    def __init__(self, head=None):
        self.head = head
        self.size = 0
        
    def insert(self, node):
        

        if not self.head:
            self.head = node
            self.size += 1
            
        else:
            # set new nodes pointer to old head
            node.nextNode = self.head
            # reset head to new node
            self.head = node
            self.size +=1

    def getNum(self,n):   # Define a new method that take a value in to return appropiate node
        mynode = self.head  # Establish
        c = 0   # start a a counter for every node
        while mynode:  # While Loop that attaces nodes
            c += 1   # Counter goes up by one
            if n == c: # if condition ~ value set by main program == counter value
                print(mynode.data)     # print (data in appropiate node)
            mynode = mynode.nextNode   # gives pointer to next node

    def getSize(self):
        return self.size

    def printLL(self):
        mynode = self.head
        c = 0
        while mynode:
            c += 1
            print(mynode.data, c)
            mynode = mynode.nextNode

    def listpop(self):   # Named a method with the initial idea to pop back values as a stack
        nodestack=[]     #Created a blank list to append node values
        mynode = self.head # set a variable equal to the node value
        
        while mynode: # Create a while loop to attach nodes to blank list
            
            nodestack.append(mynode.data) # Method that appends data from my node to list 
            mynode = mynode.nextNode # gives pointter to the next node

        return(nodestack[::-1]) #returns new list backwards 
            
