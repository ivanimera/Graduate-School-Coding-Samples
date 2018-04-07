#Unit 3 Assignment 1
#
#Author: Ivan Mera
#
# Finding Harshard numbers for range(1,501)
# Created a blank list
harlist=[]
# Defined an isharshad function that grabs an integer and returns a boolean
#value depending on whether integer is a harshad number or not

def isharshad(n):
    a =list(str(n)) # Use a variable to first cast an integer as str and immidiately
                    # separates the digits by converting the strings to a list
    accum = 0     #Set an accum to add the digits into in order to perform operation
#Created a definite loop that grabs the individual digits and adds them to the
#accumulator.Finally the function returns a boolean value depending on whether
# the number is a harshad or not by using a modulus operation
    for i in a:
        accum = accum + int(i)
    return n % accum == 0 # if a number is divisible by the sum of its digits,
                          #then its remainder would be zero

for i in range(1,501):   #Iterates every integer in the range(1,501)
    if isharshad(i) == True: #Set a condition for integer results in isharshad function
        harlist.append(i) #if integer is a harshard number then it appends it to created list
print("Here is a list of all\
 harshad numbers in the list: ",harlist)   # It ultimately prints list of HARSHAD values.


#ZERO NOT INCLUDED IN RANGE, CANNOT DIVIDE BY ZERO
