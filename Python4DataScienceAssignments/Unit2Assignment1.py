#assignment1unit2
#
#
#Author: Ivan Mera
#
'''
Write a program that prints the numbers from 1 to 100.
But for multiples of three print “Cow” instead of the number and for the multiples of seven print “Pie”.  
For numbers which are multiples of both three and seven print “CowPie"'''


# First I created an blank list to fill in with values from the loop I created
MyList2 = []

#Used 'for' to set up a definite loop in the range(1,101,1)
#It does not contain zero and includes 100
#I used the append function to add the values asked to the list
#I printed the list in the end of the program

for i in range(1,101,1):
    if i%3==0 and i%7==0: #Using IF, ELIF, anf ELSE, I set a loop where
                          # I assign cowpie, cow, and pie to values
                          #where i are multiples of '7 & 3', '3', and, '7' respectively
        MyList2.append("cowpie")
    elif i%3==0:
        MyList2.append("cow") 
    elif i%7==0:
        MyList2.append("Pie")
    else:
        MyList2.append(i)

print(MyList2)
