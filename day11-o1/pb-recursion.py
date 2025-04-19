## ~~~~~~~~~~~~~~ factorial sequence ~~~~~~~~~~~

def findFact(n):
    if n <=1:
        return n 
    return  n * findFact(n -1 )


print(findFact(5))  ## 120 




## ~~~~~~~~~~~~~ fibonacci sequence ~~~~~~~~~~~~~~


def findFIb(n):
    if n <= 1:
        return n 
    return findFIb(n- 1) + findFIb(n -2 )

print(findFIb(5)) ## 5 
print(findFIb(6)) ## 8 
print(findFIb(7)) ## 13 

## time - o(2^n) : exponential time which is too huge 

## note: to find the time complexity for recursive code, first draw recurrence relation and then solve it using any of three methods such as substitution method, Recursive tree method, and Master theorem

## space - o(n) : stack data structure is used to store all the recursive calls. 


## ~~~~~~~~~~~~ sum of digits ~~~~~~~~~~~~~~~~~~~~


def sumOfDigits(n):
    ## base case 
    if n < 9:
        return n 
    
    ## recursive call 
    return n % 10 + sumOfDigits(n // 10)

print(sumOfDigits(12345)) ## 15  




## ~~~~~~~~~~~~~ Power of an element ~~~~~~~~~~~~~~~


## approach 01 :

def pow(a, n):
    ## base case 
    if n == 0:
        return 1 
    ## normal recursive call 
    return a * (pow(a, n -1 ))


print(pow(2,8))  ## 256

