## given numbers from 1 to N- except one number is missing. Find the missing number

## https://leetcode.com/problems/missing-number/description/

## method 01 : BRUTE FORCE -
def missingNumber(arr, n):
    for i in range(1,n+ 1):
        if i not in arr: ## this membership check in array also takes o(n) time 
            return i 
        

## time - o(n2)
## space - o(1)

print(missingNumber([1,3,4,5], 5))



## Method 02 :
## Optimal approach - using hash_set 

def missingNumber2(arr, n):
    ## step1 - convert the array into a set 
    hashSet = set(arr)  ## set formation takes o(n) time 

    ## step2 : fo a check for 1 to n numbers in set
    ## membership in set takes O(1) time, and since we do this for n elem, total time to check all elem in set - o(n)


    for i in range(1, n + 1 ):
        if i not in hashSet:
            return i 
        
print(missingNumber2([1,3,4,5], 5)) ## 2


## Time - O(n)
## space - O(n)

## Using hash-dictionary 

def missingNumberUsingDict(arr,n):
    hashMap = {}
    for i in arr:
        hashMap[i] = True 

    for i in range(1, n+1 ):
        if i not in hashMap:
            return i 
        

print(missingNumberUsingDict([1,2,3,5], 5)) ## 4



## NOTE: 
# - hashing using set or dict works great in python. 
# - it gives us fast lookup and simple code. 





## Method 03: 
## Optimal approach - sum formula 
def missingNumber3(arr, n):
    # x = len(arr)
    return (n* (n+1))//2 - sum(arr)


print(missingNumber3([1,2,3,4,6],6)) ## 5


## Time - O(n)
## space - o(1)

## this is a nice approach but sometimes, there can be a case of overflow - maybe when array elements are huge. 
## so better always go for xor ops 

## in case n = 10^9, n is too huge, doing (n * n+1 )//2 will reuslt in overflow problem.


## XOR never exceeds the largest number 




## METHOD 04: 
## most optimal approach - XOR 


## NOTE: 
## x ^ x = 0 and x ^ 0 = x

def missingNumber4(arr, n):
    xor1 = 0
    for i in range(1, n+1 ):
        xor1 ^= i

    for i in arr:
        xor1 ^= i

    return xor1 

print(missingNumber4([1,3,4,5], 5)) ## 2 


## Time - o(n)
## space - o(1)

