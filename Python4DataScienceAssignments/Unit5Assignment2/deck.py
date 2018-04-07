#Deck of Cards
#
#
#Author:Ivan
#
import random              #Import Random module to use functions

class card(object):       #create a card class
     
     def __init__(self, suit, Number):    #Constructor with suit and number
          self.Number = Number            # attribute suit and number
          self.suit = suit                 # 2 instance variables
     
     def getSuit(self):     #Getter returns suit value
          return self.suit    
     
     def GetNumber(self):     #Getter sets a variable equal to the card number
          v = self.Number
          Numbers = {11: 'J', 12: 'Q', 13: 'K', 14: 'A'}
          if v<=10:
               return v       # Conditional uses numbers for 1 to 10
          else:
               return Numbers[v]  #  If JQKA, it uses dictionary value
               
     def getCardNum(self):       #Getter allows for to have suits to join number
          s = self.getSuit()
          v = self.GetNumber()
          
          suits = {'C': 0, 'D': 15, 'H': 30, 'S': 45} 
          Numbers = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
          
          if v in Numbers:                 #if conditional to merge number
               return Numbers[v]+suits[s]   #accounts for JQKA
          
          return v+suits[s]         #Combines number in card with suits

     
class deck(object):             #design a class for deck of cards
     def __init__(self):                #constructore that calls on itself
          self.deck = []   #Blank List
          suits = ['C', 'D', 'H', 'S']    # Suits list defined here
          for s in suits:                 # for CDHS in suits list
               for v in range(2, 15):
                    self.deck.append(card(s, v)) # Range function appends suit and value to list
                                                #takes into consideration card class methods
     def getDeck(self):         #Getter allows us to get deck
         return self.deck
        
     def deal(self):               #deal method allows us to pick a card
          return self.deck.pop(0)

     def shuffleDeck(self):        #method allows us to shuffle using random module
          random.shuffle(self.deck)
          
     def fan(self):                #prints all card values on the deck to be seen
          for c in self.deck:
               print ("{}{}".format(c.GetNumber(), c.getSuit()))

     def isOrdered(self):            # a method that returns true if its in order and false if its not
            for i in range(len(self.deck)-1):
                if self.deck[i].getCardNum()>self.deck[i+1].getCardNum():
                    return False

            return True

     def compareCards(self, card1, card2):       # Method allows us to compare values and return a value
         card1Number = card1.getCardNum()
         card2Number = card2.getCardNum()
         if card1Number < card2Number:
             return -1
         else:
             return 0
    
     def order(self):             # Allows us to sort the deck of cards
         self.deck.sort(lambda x, y: self.compareCards(x, y))
