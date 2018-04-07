#Unit 3 Assignment 2
#
#Author: Ivan Mera
#
#A program that evaluates numbers on a file and categorizes them into three
#categories.

#As a first step, imported needed functions from mylib.py module
import mylib

#Then proceeded to open file, read and assign data to a variable and close file
infile = "Rumbers.txt"
nums = open(infile, 'r')
data = nums.read()
nums.close

#Two empty lists and an output file were created to to help in solving assignment
#HarshSiete list will hold numbers to later write into Outfile 'HarshOut.txt.'
#HSHodge holds values that meet all three conditions asked in assignment
HarshSiete = []
HSHodge =[]
Outfile = open("HarshOut.txt",'w') #File was created here
# Steps were take to clean data from original file
data = data.replace('\n','\t') # Lines were deleted by replacing line
                               #separations with tabs

data = data.split('\t') # Split function was used to separate strings into a list
#Data strings were casted as integers to work with already defined functions
data = [int(i) for i in data] 
#An accumulator was set to hold the sum of all Harshad numbers
accum = 0
#A loop was created that allowed functions to iterate throughout the list
#to determine which variables meet which requirements
for i in data: 
    if mylib.isharshad(i) == True: #Conditional to find wich values are Harshad
        accum = accum + i #accum keeps adding all values that are Harshad
    #Second condition set where harshard must be divisible by seven as well
    if mylib.isharshad(i) == True and mylib.isSiete(i) == True:
        HarshSiete.append(i) # append function used to attach values that meet condition
#Last condition set where numbers must meet the first two conditions and be evenly divisible by 14
    if mylib.isharshad(i) == True and mylib.isSiete(i) == True and i % mylib.Hodges == 0:
        HSHodge.append(i)   #append values that meet all three conditions 
#Set a loop where values from second if statement are met and add them to file HarshOut.txt    
for i in HarshSiete:
    Outfile.write(str(i) + '\n')  

Outfile.close() #close file to save designated values into file

#Print sum of Harshad values
print("The sum of all Harshard numbers in the list is equal to:",accum)
print("****************************************************************")
#Print values that are Harshad numbers and divisible by 7
print("All numbers that are Harshad numbers\
 and whose tenths digits are equal to seven:\n",HarshSiete)
print("****************************************************************")
#Print values that meet all three conditions
print("Finally, all numbers that are Harshad, whose tenths digits are equal\n\
is equal to seven and that are divisible by 14 are:", HSHodge)

#I am aware I do not need to put == True but in my opinion you can see the logic
#better by doing so. 

    
