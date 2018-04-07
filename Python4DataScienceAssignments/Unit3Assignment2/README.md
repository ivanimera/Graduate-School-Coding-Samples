In this assignment we will be reading from and writing to files and creating a library that you will import for use in your main program.

Givens:

I have created a text file, Rumbers.txt, that contains 5000 random numbers.  These numbers are stored in ten columns.  The columns are separated by tabs and rows end with a newline.  This file resides in your Unit 3 resources.

You already have your isHarshad() function from assignment 1.  We are going to use it here.  

The Task:

You need to find/create three things

1. The sum of the Harshad numbers in ‘Rumbers.txt’.
2. An output file containing all the Harshad numbers with a ‘7’ in the tens place.
3. The numbers that are Harshad, have a 7 in the second column and are evenly divisible by the constant ‘Hodges’.

The Hows or “What we need to see”

You need to provide three files.

1. A file called “myLib.py”  Inside this file should reside two functions, isHarshad() and Siete().  isHarshad() will accept an integer and return True if the input is a Harshad number and False if it is not.  isSiete() will accept an integer and will return True if the second column digit (The ‘tens’ column) of the number is a ‘7’ and False if it is not.  Lastly, you are to create a constant variable called “Hodges” and set it equal to 14.  All three of these items will be imported by your main program.

2. A main program (mainprog.py?) that reads in “Rumbers.txt” and creates the three deliverables listed above.  This main program will open Rumbers.txt, import functions and the Hodges variable from myLib.py, do the processing necessary to find the solutions and create the output file we need, and then will close “Rumbers.txt” and the output file (see below).  As output (to the screen) this program will print out the sum of the Harshad numbers and print the numbers that are harshad numbers with a seven in the tens column and are also multiples of the Hodges constant.

3. An output file named “HarshOut.txt” that contains all of the Harshad numbers that have a ‘7’ in their second column.

If this seems complicated, rest assured that it is not; once you get rolling it will be fun.  Email me with any questions.  Good luck.
