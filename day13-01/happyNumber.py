## ~~~~~~~~~~~~~~~ happy number ~~~~~~~~~~~~~~~~


## Write an algorithm to determine if a number n is happy.

## A happy number is a number defined by the following process:

## Starting with any positive integer, replace the number by the sum of the squares of its digits.
## Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
## Those numbers for which this process ends in 1 are happy.
## Return true if n is a happy number, and false if not.



def happyNumber(n):
    ## we want to store all the n values, so that when it repeats, we find it and well ends the ops. 
    ## we are using set as lookup time in set is o(1)
    seenSet = set()
    while n != 1:
        if n not in seenSet:
            seenSet.add(n)
            n = sum(int(i)**2 for i in str(n))
        else:
            return False 

    return True 


## time - o(logn)
## space - O(1)

     