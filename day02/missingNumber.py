## ~~~~~~~~~~ Find the missing number ~~~~~~~~~~~~~

## leetcode : 268- easy

## Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.


## Input: nums = [3,0,1]

## Output: 2

## Explanation:

## n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.


## method 01 : 
def missingNumber(arr):
    n = len(arr)

    ## we use summation of numbers formula to track down the missing number 

    return (n* (n + 1 )) // 2 - sum(arr)


print(missingNumber([3,0,1])) ## 2 

## ~~~~~~~~~~~~~~~~~~~


## method 02 : Using XOR operation 

def missingNumber2(arr):
    ## using Xor 
    xor1 = arr[0]
    for i in range(1,len(arr)):
        xor1 ^= arr[i]

    for i in range(0, len(arr) + 1):
        xor1 ^= i 

    return xor1 

print(missingNumber2([3,0,1])) ## 2

## Time complexity: O(n)
## Space complexity: O(1)

