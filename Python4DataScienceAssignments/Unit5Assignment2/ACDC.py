#ACDC game
#
#Author: Ivan
#
#An interactive Acey ducey betting game

import random                  #Import Random module to use functions

import deck                        #Import card deck file

class ACDC(object):                          #create a class for the game
    def __init__(self, BankNumber):
        self.gameDeck = deck.deck()               # create instance value for pot
        self.Bank = BankNumber               #set variables for user and bank pot
        self.User = BankNumber
        
    def Bankturn(self):
        self.gameDeck.shuffleDeck()           # Shuffle Deck method

        num1 = random.randint(0, len(self.gameDeck.deck)-1)  # random card chosen for card 1 and 2
        card1 = self.gameDeck.deck.pop(num1)                # card chosens from deck 
        num2 = random.randint(0, len(self.gameDeck.deck)-1)
        card2 = self.gameDeck.deck.pop(num2)

        if card1.getCardNum()>card2.getCardNum():     # conditional considers if card1 is bigger than card 2
            return [card2, card1]           #it returns the card's values
        return [card1, card2]
    
    def UserTurn(self):                     #Method that deals card (from import deck.py and returns card     
        UserCard = self.gameDeck.deal()           
        return UserCard

    def bet(self):                # Metho that asks for user to enter wager and shows range

        BankCards = self.Bankturn()
        BankNum1 = BankCards[0].getCardNum()    #variables that will help display value
        BankNum2 = BankCards[1].getCardNum()
        print ("{}-[{},{}]".format("The range is between ","{}{}".format(BankCards[0].GetNumber(), BankCards[0].getSuit()), "{}{}".format(BankCards[1].GetNumber(), BankCards[1].getSuit())))
        # print statement shows the user the range of the cards to place acdc
        AmtBet = int(input("Please Enter the Wager: "))    #variable with input function for wager

        if AmtBet>self.User:
            print ("User has insufficient funds!")       #conditional blocks user from betting more than they have
            return False
        
        
        UserCard = self.UserTurn()                   #variable for dealt card
        
        UserNum = UserCard.getCardNum()              #variable that gets card number
        

        if UserNum>=BankNum1 and UserNum<=BankNum2:   # Conditional statement that proves if card number is in between both dealt cards
            self.User+=AmtBet              #Adds to player amount and reduces from bank pot
            self.Bank-=AmtBet
            print ("User Won")        #prints player won
        else:                              #else if bank wins
            self.Bank+=AmtBet
            self.User-=AmtBet        #accum functions that add to bank and substract from  user
            print ("Bank Won")         #print bank wons

        print ("{}:{}".format("User - ", self.User))
        print ("{}:{}".format("Bank - ", self.Bank))
        
        return True

if __name__=='__main__':
    Bank = int(input("Please enter initial pot amount: "))    #asks user to present initial pot amount
    game = ACDC(Bank)         #sets function for acdc game
    flag = False
    while game.User>0 and game.Bank>0:   # while loop allows game to continue as long as there is 
        if not game.bet():
            flag = True                  #Value that changes as loop rechecks values, flag placed to change is values are less than zero
        if flag:
            if game.User==0:              #if condition that displays user pot = 0
                print ("User is out of luck")          #Shows the user has runt out money
            else:
                print ("Bank Lost To The User")     # Displays the bank lost its pot
            exit()

    if game.User==0:                              
        print ("User is out of luck")        # Shows the user is out of funds
    else:
        print ("Bank Lost To The User")       #Shows bank has lost money in pot . 
