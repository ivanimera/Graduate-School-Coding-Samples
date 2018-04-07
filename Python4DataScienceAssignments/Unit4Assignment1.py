#EXPONENTIATION
#
# Author: Ivan Mera
#
#Writing a program that finds a number to a power


def myPow( num, exp):  # define function
    if exp == 1:       # if exp ==1 returns number
        return num
    else :
        return num * (myPow(num, (exp-1))) # recursively solves exponent problem

a = myPow (7,3) # assigns return value to variable
print (a)       #prints variable
b = myPow (2,6)   # assigns return value to variable
print(b)        #prints variable

c = myPow(5,10)   # assigns return value to variable
print(c)            #prints variable
