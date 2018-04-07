#Unit 4 Assignment 2
#
#Author: Ivan Mera
#
#A program that cleans, sorts, and searches for numbers in a file

import mysearch                 #import library

infile = "rands.txt"            #call out file
nums = open(infile, 'r')        #open file
data = nums.read()              # add file to list
nums.close                      #close file

data = data.replace('\n', '\t') #clean data

data = data.split('\t')         # split string in to list

data = [int(i) for i in data]   #turn str list into int list

data.sort()                     #sort data with python module

#Binary Search Results using functino from imported library
mysearch.bsearch(78700,data)
mysearch.bsearch(3333,data)
mysearch.bsearch(1118,data)

#Linear search using function from imported library
mysearch.lsearch(78700,data)
mysearch.lsearch(3333,data)
mysearch.lsearch(1118,data)
