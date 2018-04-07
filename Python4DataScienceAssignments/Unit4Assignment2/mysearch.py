# this is a comment
#
# Author Lars  ~~~slightly modified by Ivan
#
#  A program to do a binary search on a list of numbers
#


def bsearch(x, nums):
    item =0
    low = 0
    high = len(nums) -1
    c = 0

    while low <= high:                   # Still a range to search
        #print("Step counter : ",c,item)
        mid = (low+high)//2              # this is the position of the middle number
        item = nums[mid]
        #print("The Mid:",item)
        
        if x == item:        # got it, now return it!
            print("the number ", x, "was found in list") #print returned value
            print("it took",c,"passes")     #print total count
            return print('index:', mid,'\n')   #print index list reference

        elif x < item:       # x is in the lower half of the range
            high = mid -1    #    move the top marker down
            c = c + 1        #    up the step counter

        else:                # x is in the upper half
            low = mid + 1    #    move the bottom marker up
            c = c + 1
    print(x,"could not be found in list")
    print("It took", c, "lookups")#    print total lookups
    return print(-1,'not found\n')      # x is not found


####
# Function for a linear search

def lsearch(x, nums):
    c = 0
    for i in range(1,len(nums)):   
        if x == nums[i]:
            c = c + 1
            print("Number Found!",nums[i])          #prints number if found
            print("Linear Search took",c,"passes\n") #prints number of passes
            return i
        else:
            c = c + 1  #counts even though number is not found
            
    print("Number not found")  # informs user number not in list
    print("The Search took",c,"passes") # informs total number of passes
    return print(-1,"not found\n")
