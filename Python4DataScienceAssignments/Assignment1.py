# Assignment 1
#
#Converting inches to feet, yards, and miles 
#
#Author: Ivan Mera
#

print("***********************")
print("*US Distance Converter*")
print("***********************\n")

# Provide instructions and a disclaimer to the user that program does not accurately convert, but offers a vague comparison.
# Inform user to not use float values because program will fail.

print("This program is not intended as an accurate converter of inches to feet, yards, and miles")
print("Its purpose is to vaguely inform the user of the distance in question.")
print("It always rounds down to the nearest foot, yard, or mile")
print("Please round your measurements to the nearest inch, no decimals or fractions!!\n")


#Ask program user to input number of inches and cast it as an integer.

inches = int(input("Please enter the number of inches: "))


''' Now I will name three variables where I convert the variable inches into
into feet, yards and miles'''

feet = inches // 12
yards = feet // 3
miles = yards // 1760


#After assigning all three measurments to three different variables I proceeded to print results similar to what is shown in example.
if feet >= 2:
    print(feet, "feet")
elif feet == 1:
    print(feet, "foot")
else:
    print("You do not have enough inches to convert to feet!")

if yards >= 2:
    print(yards, "yards")
elif yards == 1:
    print(yards, "yard")
else:
    print("You do not have enough feet to convert to yards!")

if miles >= 2:
    print(miles, "miles")
elif miles == 1:
    print(miles, "mile")
else:
    print("You do not have enough yard to convert to miles!")
    
