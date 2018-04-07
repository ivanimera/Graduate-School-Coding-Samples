#Unit 3 Assignment 2
#
#Author: Ivan Mera
#
# Defined an isharshad function that grabs an integer and returns a boolean
#value depending on whether integer is a harshad number or not
def isharshad(n):
    a =list(str(n))# Use a variable to first cast an integer as str and immidiately
                    # separates the digits by converting the strings to a list
    accum = 0 #Set an accum to add the digits into in order to perform operation
#Created a definite loop that grabs the individual digits and adds them to the
#accumulator.Finally the function returns a boolean value depending on whether
# the number is a harshad or not by using a modulus operation
    for i in a:
        accum = accum + int(i)
    return n % accum == 0# if a number is divisible by the sum of its digits,
                          #then its remainder would be zero

#Defined a variable that looks at tenths digit and sees if it equals seven
def isSiete(n):
 a = str(int(n)//10) #Casts value as integer and then as string
 return a[-1] == '7' #Used division that gives back a float and eliminates
                     #ones digit. Then asked function to return boolean value
                     #whether new ones digit equals string 7

Hodges = 14 #Set constant to be used in main program
