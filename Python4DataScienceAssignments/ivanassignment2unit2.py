#Assignment2Uni2
#
#
#Author: Ivan Mera
#
#
#

'''Instructions 
MyList = [ 23, -45, 6, -23, -9, 77, 54, -54, 21, -2, 8, -3, -23, 45, 93, -43, 999, -2, 3, 78, 90 ]

Given the list above write a program that prints out the average of the negative numbers
in the list before the value 999.
'''

MyList = [ 23, -45, 6, -23, -9, 77, 54, -54, 21, -2, 8, -3, -23, 45, 93, -43, 999, -2, 3, 78, 90 ]
accum = 0
count = 0
#I set an accumulator and a counter to add i and number of i (respectively) for all instances where i!=999 and i <0 using a condition within another condition
#I used break command to remove me from the loop once it reaches 999
# Afterwards I assigned Python to print accum divided by count to have average.

for i in MyList:
    if i!= 999:
        if i <0:
            accum = accum + i
            count = count+ 1
    else:
       break


print(accum/count)
