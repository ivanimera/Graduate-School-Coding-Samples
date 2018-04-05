#Assignment #2
#
#Guess my weight!!!!
#
#Author: Ivan Mera
#

print("************************")
print("****GUESS MY WEIGHT!****")
print("************************\n")

# Provide instructions to user on guessing game.

print("Professor Lars and Professor Hans! Welcome to Guess My Weight!")
print("Please try to guess my age and weight correctly!")
print("If you guess both correctly, you will get a Python High 5")
print("Please only use positive integers!")

#I have assigned two hard coded variables to represent my age and weight 
correct_age = 27
correct_weight = 198
print("\n")

#Using the utility function input and casting the user's input with integer, I created a numerical value
#to compare the users' inputs with the correct answers in the assigned variables.

guess_age = int(input("Enter your guess for age: "))

guess_weight = int(input("Enter your guess for age: "))

# Using a mix of complex conditional expressions with Boolean operators and Comparison conditionals,
# I wrote a program that resembles the example in the assignment. I tried the exercise with the numbers
# given in the example and had the same results.
# After seeing that the program worked as intended, I replaced the hard coded values with my actual age and weight.

#IF GUESSED AGE AND GUESSED WEIGHT ARE HIGHER, CONDITION PRINTS BOTH HIGHER.
#IF GUESSED AGE AND GUESSED WEIGHT ARE LOWER, CONDITION PRINTS BOTH LOWER.
#IF GUESSED AGE AND GUESSED WEIGHT ARE CORRECT, CONDITION PRINTS BINGO.
#FOR ALL ELSE, CONDITION PRINTS GAME OVER


if ((guess_age > correct_age) and (guess_weight > correct_weight)):
    print("Both Higher")
elif ((guess_age < correct_age) and (guess_weight < correct_weight)):
    print("Both Lower")
elif ((guess_age == correct_age) and (guess_weight == correct_weight)):
    print("BINGO!")
else:
    print("Game Over")
    
