#
#   Use the linked list class
#

from linkedlist import *

MyList = linkedList()

MyList.insert(Node("Lars"))
MyList.insert(Node("Alex"))
print(MyList.getSize())
MyList.insert(Node("Michael"))
print(MyList.getSize())
MyList.insert(Node("Abhi"))
              
# Use my print method
MyList.printLL()
print("*****************************")
print('\n')

MyList.getNum(2) # call getNum method for MyList
