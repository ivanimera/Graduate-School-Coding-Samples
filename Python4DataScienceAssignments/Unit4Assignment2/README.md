In your Unit 4 resources folder is a file called rands.txt.  It is a file of 10,000 randomly generated numbers between 1 and 100,000.  

You will:

Read in this file, clean the data, convert from strings to integers and then sort the data.  At the end of this process you should have a list of sorted integers with a len of 10,000.

Create a library called mySearches.py.  In this module two functions should reside:

bsearch - a function that accepts an integer and a list.  The function should conduct a binary search through the list and return the index of the number in the list if the number is found and a -1 if the number is not found.  The function should report how many lookups were performed during the search before it returns its value.

lsearch - a function that accepts an integer and a list.  The function should conduct a linear search through the list and and return the index of the number in the list if the number is found and a -1 if the number is not found.  The function should report how many lookups were performed during the search before it returns its value.

A main program called lookup.py should import both functions from mySearches.py.  In the body of the program you should search for three numbers in the data (78700, 3333, 1118).  Output should show if the number was found in the list and how many lookups were needed for each kind of search, even if the number is not found in the list.
